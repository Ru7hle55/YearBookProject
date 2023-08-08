from django.contrib import admin
from MyYearBookProject.photos.models import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'photo_name',
        'date_of_publication',
        'description',
        'get_tagged_stories',
    )

    @staticmethod
    def photo_name(obj):
        return obj.photo.name

    @staticmethod
    def get_tagged_stories(obj):
        return ', '.join([story.name for story in obj.tagged_stories.all()])


# Register your models here.
admin.site.register(Photo, PhotoAdmin)
