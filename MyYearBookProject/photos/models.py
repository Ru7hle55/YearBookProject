from django.db import models

from MyYearBookProject.accounts.models import ProjectUser
from MyYearBookProject.stories.models import Story
from MyYearBookProject.photos.validators import validate_image_size
from django.core.validators import MinLengthValidator


# Create your models here.
class Photo(models.Model):
    photo = models.ImageField(
        blank=False,
        null=False,
        validators=[validate_image_size],
        upload_to='images'
    )
    description = models.TextField(
        blank=True,
        null=True,
        max_length=300,
        validators=[MinLengthValidator(10)],
    )
    location = models.CharField(
        blank=True,
        null=True,
        max_length=30,
    )
    tagged_stories = models.ManyToManyField(
        Story,
        blank=True,
    )
    date_of_publication = models.DateField(
        auto_now=True,
    )
    user = models.ForeignKey(to=ProjectUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'ID: {self.pk} - Name: {self.photo.name}'
