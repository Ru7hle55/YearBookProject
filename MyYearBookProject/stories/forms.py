from django import forms
from MyYearBookProject.stories.models import Story


class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = [
            'name',
            'date_of_story',
            'story_photo',
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Story name',
            }),
            'date_of_story': forms.DateInput(attrs={
                'type': 'date',
            }),
            'story_photo': forms.TextInput(attrs={
                'placeholder': 'Link to Image',
            }),
        }
        labels = {
            'name': 'Story Name',
            'date_of_story': 'Date of Story',
            'story_photo': 'Link to Image',
        }


class StoryDeleteForm(StoryForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
