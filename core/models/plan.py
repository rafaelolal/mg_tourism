from django.urls import reverse

from django.db import models
from django.db.models.fields import BooleanField, CharField, TextField
from django.db.models.fields.related import ForeignKey, ManyToManyField

from .thing import Thing
from .user import UserProfile

class Plan(models.Model):
    name = CharField(max_length=64)
    description = TextField(max_length=512)
    is_public = BooleanField()
    
    owner = ForeignKey(UserProfile, on_delete=models.DO_NOTHING, related_name='plans')
    things = ManyToManyField(Thing, related_name='plans_in')
    favorited_by = ManyToManyField(UserProfile, related_name='favorited')

    def get_absolute_url(self):
        return reverse("core:user_detail", kwargs={"pk": self.owner.pk}) + "?my_plans"
    