from django.db import models

from MyYearBookProject.accounts.models import ProjectUser
from MyYearBookProject.common.validators import validate_comment_text
from MyYearBookProject.photos.models import Photo


class Comment(models.Model):
    comment_text = models.TextField(
        max_length=300,
        blank=False,
        null=False,
        validators=[validate_comment_text,],
    )
    date_and_time_of_publication = models.DateTimeField(
        auto_now_add=True,
    )
    to_photo = models.ForeignKey(to=Photo, on_delete=models.CASCADE)
    user = models.ForeignKey(to=ProjectUser, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_and_time_of_publication']


class Like(models.Model):
    to_photo = models.ForeignKey(to=Photo, on_delete=models.CASCADE)
    user = models.ForeignKey(to=ProjectUser, on_delete=models.CASCADE)
