from django import forms
from MyYearBookProject.common.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'comment_text',
        ]
        widgets = {
            'comment_text': forms.Textarea(attrs={
                'placeholder': 'Add comment...',
            })
        }


class SearchForm(forms.Form):
    story_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search by story name...'
            }
        )
    )
