from django.contrib import admin
from MyYearBookProject.accounts.models import ProjectUser


class ProjectUserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'CHOICES',
        'first_name',
        'last_name',
        'email',
        'gender',
        'get_user_name',
    )
    list_filter = (
        'gender',
    )
    ordering = ('id',)


# Register your models here.
admin.site.register(ProjectUser, ProjectUserAdmin)
