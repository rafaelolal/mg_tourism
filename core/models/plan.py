from django.db import models

from django.db.models.fields.related import ForeignKey, OneToOneField

from .thing import Thing
from .user import UserProfile
class Plan(models.Model):
    owner = ForeignKey(UserProfile, on_delete=models.CASCADE)

class PlanThing(models.Model):
    thing = OneToOneField(Thing, on_delete=models.CASCADE)
    plan = ForeignKey(Plan, on_delete=models.CASCADE)