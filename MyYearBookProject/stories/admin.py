from django.contrib import admin
from MyYearBookProject.stories.models import Story


# Register your models here.
class StoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)


admin.site.register(Story, StoryAdmin)
