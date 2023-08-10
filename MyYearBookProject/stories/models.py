from django.db import models
from django.template.defaultfilters import slugify

from MyYearBookProject.accounts.models import ProjectUser


# Create your models here.
class Story(models.Model):
    name = models.CharField(
        blank=False,
        null=False,
        max_length=30,
    )
    story_photo = models.URLField(
        blank=False,
        null=False,
    )
    date_of_story = models.DateField(
        blank=True,
        null=True,
    )
    slug = models.SlugField(
        unique=True,
        editable=False,
    )
    user = models.ForeignKey(to=ProjectUser, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.id}')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
