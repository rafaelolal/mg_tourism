from random import randint

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

from django.db.models.fields import BooleanField, CharField, PositiveSmallIntegerField, SmallIntegerField, TextField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey

class Thing(models.Model):
    name = CharField(max_length=64)
    short_description = TextField()
    long_description = TextField()
    address = CharField(max_length=128)
    stars = PositiveSmallIntegerField(null=True,
        blank=True)

    categories = ['Attraction', 'Tour', 'Food', 'Outdoor', 'Shopping']
    tuple_categories = [(c.lower().replace(' ', '_'), c) for c in categories]
    category = CharField(max_length=64, choices=tuple_categories)
    covid_safe = BooleanField()

    def get_picture(self):
        pictures = self.picture_set.all()
        if len(pictures):
            return pictures[randint(0, len(pictures)-1)]

    def calculate_stars(self, new_rating):
        N = len(self.comment_set.all())+2
        self.stars = round((self.stars * (N-1) + new_rating) / N, 1)
        self.save()

    def get_fields(self):
        category = eval(f"{self.category.capitalize()}")
        obj = eval(f"self.{self.category}".lower())
        fields = self.remove_unwanted_keys({field.name: field.value_to_string(obj) for field in category._meta.fields})

        return fields

    def remove_unwanted_keys(self, fields):
        unwanted = 'id name short_description category thing_ptr'.split(' ')
        for key in unwanted:
            del fields[key]

        return fields

    def get_absolute_url(self):
        return reverse(f"core:thing_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.name} | {self.category}"

class Picture(models.Model):
    thing = ForeignKey(Thing, on_delete=models.CASCADE, null=True)
    image = ImageField(upload_to='thing_pics')

    def get_absolute_url(self):
        return reverse(f"core:thing_detail", kwargs={"pk": self.thing.pk})

class Comment(models.Model):
    title = CharField(max_length=128)
    content = TextField(max_length=4096)
    rating = SmallIntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])

    thing = ForeignKey(Thing, on_delete=models.CASCADE)
    author = ForeignKey(User, on_delete=models.CASCADE)
    def get_absolute_url(self):
        return reverse(f"core:thing_detail", kwargs={"pk": self.thing.pk})