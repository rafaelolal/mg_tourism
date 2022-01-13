from django.db import models
from django.db.models.fields import BooleanField, CharField, SmallIntegerField
from django.db.models.fields.related import ForeignKey, OneToOneField, ManyToManyField

from .thing import Thing
from .user import UserProfile

class Plan(models.Model):
    name = CharField(max_length=64)
    is_public = BooleanField()
    liked_by = ManyToManyField(UserProfile, related_name='likes')
    owner = ForeignKey(UserProfile, on_delete=models.CASCADE)


class PlanThing(models.Model):
    thing = OneToOneField(Thing, on_delete=models.CASCADE)
    plan = ForeignKey(Plan, on_delete=models.CASCADE)