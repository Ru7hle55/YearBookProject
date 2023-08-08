from django import forms
from MyYearBookProject.photos.models import Photo


class PhotoCreateForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['user']
        labels = {
            'tagged_stories': 'Tag Story:',
        }


class PhotoEditForm(PhotoCreateForm):
    class Meta(PhotoCreateForm.Meta):
        exclude = [
            'photo',
            'user',
        ]
