from django.db import models
from django.contrib.auth.models import User

from django.db.models.fields.related import ForeignKey, OneToOneField

from .thing import Thing

class Plan(models.Model):
    owner = ForeignKey(User, on_delete=models.CASCADE)

class PlanThing(models.Model):
    thing = OneToOneField(Thing, on_delete=models.CASCADE)
    plan = ForeignKey(Plan, on_delete=models.CASCADE)