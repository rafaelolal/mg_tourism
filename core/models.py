from random import randint

from django.db import models
from django.contrib.auth.models import User

from django.db.models.fields import BooleanField, CharField, DurationField, PositiveSmallIntegerField, SmallIntegerField, TextField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey, OneToOneField

# Create your models here.
class UserProfileInfo(models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE)

    profile_pic = ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username

#################################################

class Thing(models.Model):
    name = CharField(max_length=64)
    description = TextField()
    address = CharField(max_length=128)
    stars = PositiveSmallIntegerField(null=True,
        blank=True)

    categories = [('attraction', 'Attraction'),
        ('tour', 'Tour')]
    category = CharField(max_length=64, choices=categories)
    covid_safe = BooleanField()

    def get_picture(self):
        pictures = self.picture_set.all()
        return pictures[randint(0, len(pictures)-1)]

    def __str__(self):
        return f"{'.'.join([word[:2] for word in self.name.split()])} | {self.category[:5]}"

class Attraction(models.Model):
    thing = OneToOneField(Thing, on_delete=models.CASCADE)
    
    types = ['Nightlife', 'Sight', 'Landmark', 'Museum', 'Fun']
    tuple_types = [(t.lower().replace(' ', '_'), t) for t in types]
    type = CharField(max_length=64, choices=tuple_types)

    neighborhood = CharField(max_length=64)

    good_for_choices = ['Kids', ' Big Groups',
        'Adrenaline Seekers',
        'a Rainy Day', 'Couples']
    tuple_choices = [(choice.lower().replace(' ', '_'), choice) for choice in good_for_choices]
    good_for = CharField(max_length=64, choices=tuple_choices)

    def __str__(self):
        return f"{'.'.join([word[:2] for word in self.thing.name.split()])} | {self.type[:5]} | {self.good_for[:5]}"

class Tour(models.Model):
    thing = OneToOneField(Thing, on_delete=models.CASCADE)
    
    types = ['Multi-day', 'City', 'Cultural', 'Historical', 'Hicking']
    tuple_types = [(t.lower().replace(' ', '_'), t) for t in types]
    type = CharField(max_length=64, choices=tuple_types)

    price = SmallIntegerField()
    duration = DurationField()

    def __str__(self):
        r = f"{'.'.join([word[:2] for word in self.thing.name.split()])} | {self.type[:5]}"
        return r

class Picture(models.Model):
    thing = ForeignKey(Thing, on_delete=models.CASCADE)
    image = ImageField(upload_to='thing_pics')

#################################################

class Plan(models.Model):
    owner = ForeignKey(User, on_delete=models.CASCADE)

class PlanThing(models.Model):
    thing = OneToOneField(Thing, on_delete=models.CASCADE)
    plan = ForeignKey(Plan, on_delete=models.CASCADE)
    
#################################################