from django.urls import path
from MyYearBookProject.stories import views
from MyYearBookProject.stories.views import StoryDeleteView

urlpatterns = [
    path('add/', views.add_story, name='add-story'),
    path('<str:username>/story/<slug:story_slug>/', views.details_story, name='details-story'),
    path('<str:username>/story/<slug:story_slug>/edit/', views.edit_story, name='edit-story'),
    path('<str:username>/story/<slug:story_slug>/delete/', StoryDeleteView.as_view(), name='delete-story'),
]
