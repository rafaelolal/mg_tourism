from django.contrib.auth.models import User
from django.urls import reverse

from django.db.models.fields import TextField
from django.db.models.fields.files import ImageField

class UserProfile(User):
    biography = TextField(max_length=512, null=True)
    profile_pic = ImageField(upload_to='profile_pics', blank=True, default='profile_pics/default.jpg')

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse(f"core:user_detail", kwargs={"pk": self.pk})