from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View

from MyYearBookProject.accounts.models import ProjectUser
from MyYearBookProject.common.forms import CommentForm
from MyYearBookProject.stories.forms import StoryForm, StoryDeleteForm
from MyYearBookProject.stories.models import Story


# Create your views here.
@login_required
def add_story(request):
    form = StoryForm(request.POST or None)
    if form.is_valid():
        story = form.save(commit=False)
        story.user = request.user
        story.save()
        return redirect('profile-details', pk=request.user.pk)

    context = {
        'form': form,
    }

    return render(request, template_name='stories/story-add-page.html', context=context)


@login_required
def details_story(request, username, story_slug):
    story = Story.objects.get(slug=story_slug)
    all_photos = story.photo_set.all()
    comment_form = CommentForm()
    is_owner = ProjectUser.objects.get(username=username)

    context = {
        'story': story,
        'all_photos': all_photos,
        'comment_form': comment_form,
        'is_owner': is_owner,
    }

    return render(request, template_name='stories/story-details-page.html', context=context)


@login_required
def edit_story(request, username, story_slug):
    story = Story.objects.get(slug=story_slug)
    if request.method == 'GET':
        form = StoryForm(instance=story, initial=story.__dict__)
    else:
        form = StoryForm(request.POST, instance=story)
        if form.is_valid():
            form.save()
            return redirect('details-story', username, story_slug)

    context = {
        'form': form,
    }

    return render(request, template_name='stories/story-edit-page.html', context=context)


# @login_required
# def delete_story(request, username, story_slug):
#     story = Story.objects.get(slug=story_slug)
#     if request.method == 'POST':
#         story.delete()
#         return redirect('profile-details', pk=request.user.pk)
#     form = StoryDeleteForm(initial=story.__dict__)
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, template_name='stories/story-delete-page.html', context=context)

class StoryDeleteView(View):
    template_name = 'stories/story-delete-page.html'

    @method_decorator(login_required)
    def get(self, request, username, story_slug):
        story = Story.objects.get(slug=story_slug)
        form = StoryDeleteForm(initial=story.__dict__)

        context = {
            'form': form,
        }

        return render(request, template_name=self.template_name, context=context)

    @method_decorator(login_required)
    def post(self, request, username, story_slug):
        story = Story.objects.get(slug=story_slug)
        if request.method == 'POST':
            story.delete()
            return redirect('profile-details', pk=request.user.pk)

        return redirect('home-page')