from random import randint
from typing import Dict, Any


from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

from django.db.models.fields import BooleanField, CharField, DurationField, PositiveSmallIntegerField, SmallIntegerField, DecimalField, TextField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey

class Thing(models.Model):
    name = CharField(max_length=64)
    short_description = TextField()
    long_description = TextField()
    address = CharField(max_length=128)
    stars = DecimalField(
        max_digits=2,
        decimal_places=1,
        null=True,
        blank=True)

    categories = ['Attraction', 'Tour', 'Food', 'Outdoor', 'Shopping']
    tuple_categories = [(c.lower().replace(' ', '_'), c) for c in categories]
    category = CharField(max_length=64, choices=tuple_categories)
    covid_safe = BooleanField()

    def get_picture(self):
        """Returns a random picture from a Thing to use in core/thing_list"""
        pictures = self.picture_set.all()
        if len(pictures):
            return pictures[randint(0, len(pictures)-1)]

    def get_fields(self) -> Dict[str, Any]:
        """Returns the name and value of specific fields in a Thing, independent of its category"""
        category = eval(f"{self.category.capitalize()}")
        obj = eval(f"self.{self.category}".lower())
        fields = self.remove_unwanted_keys({field.name: field.value_to_string(obj) for field in category._meta.fields})

        return fields

    def remove_unwanted_keys(self, fields: Dict[str, Any]) -> Dict[str, Any]:
        """Removed unwanted values from fields"""
        unwanted = 'id name short_description category thing_ptr'.split(' ')
        for key in unwanted:
            del fields[key]

        return fields

    def get_absolute_url(self):
        return reverse(f"core:thing_detail", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return f"{self.name} | {self.category}"

# Inhereting from Thing instead of assigning a ForeignKey field
# because I want to use CreateViews and different categories have different fields/values
# Not inhereting would force me to create a ThingCreateView with many changes
# and a Form for each category
class Tour(Thing):
    category = 'Tour'

    types = ['Multi-day', 'City', 'Cultural', 'Historical', 'Private']
    tuple_types = [(t.lower().replace(' ', '_'), t) for t in types]
    type = CharField(max_length=64, choices=tuple_types)

    price = DecimalField(max_digits=9, decimal_places=2)
    duration = DurationField()

    def get_absolute_url(self):
        return reverse("core:thing_detail", kwargs={"pk": self.pk})

# Attraction, Food, Outdoor, and Shopping have the same fields but with different values
class Attraction(Thing):
    types = ['Nightlife', 'Sight', 'Landmark', 'Museum', 'Fun']
    tuple_types = [(t.lower().replace(' ', '_'), t) for t in types]
    type = CharField(max_length=64, choices=tuple_types)

    neighborhood = CharField(max_length=64)

    good_fors = ['Kids', 'Big Groups',
        'Adrenaline Seekers',
        'a Rainy Day', 'Couples']
    tuple_choices = [(choice.lower().replace(' ', '_'), choice) for choice in good_fors]
    good_for = CharField(max_length=64, choices=tuple_choices)

    def get_absolute_url(self):
        return reverse("core:thing_detail", kwargs={"pk": self.pk})

class Food(Thing):
    types = ['Farmers Market', 'Breweries and Wine', 'Coffee Shop', 'Restaurant', 'Bar']
    tuple_types = [(t.lower().replace(' ', '_'), t) for t in types]
    type = CharField(max_length=64, choices=tuple_types)

    neighborhood = CharField(max_length=64)

    # using the same good_fors from attraction
    good_fors = Attraction.good_fors
    tuple_choices = [(choice.lower().replace(' ', '_'), choice) for choice in good_fors]
    good_for = CharField(max_length=64, choices=tuple_choices)

    def get_absolute_url(self):
        return reverse("core:thing_detail", kwargs={"pk": self.pk})

class Outdoor(Thing):
    types = ['Wildlife Exploration', 'Hiking', 'Biking', 'Zoos', 'River Rafting']
    tuple_types = [(t.lower().replace(' ', '_'), t) for t in types]
    type = CharField(max_length=64, choices=tuple_types)

    neighborhood = CharField(max_length=64)

    # using the same good_fors from attraction but removing a single value
    good_fors = Attraction.good_fors.copy()
    good_fors.remove("a Rainy Day")
    tuple_choices = [(choice.lower().replace(' ', '_'), choice) for choice in good_fors]
    good_for = CharField(max_length=64, choices=tuple_choices)

    def get_absolute_url(self):
        return reverse("core:thing_detail", kwargs={"pk": self.pk})

class Shopping(Thing):
    types = ['Gift Shops', 'Shopping Malls', 'Antique Stores', 'Department Stores', 'Factory Outlets']
    tuple_types = [(t.lower().replace(' ', '_'), t) for t in types]
    type = CharField(max_length=64, choices=tuple_types)

    neighborhood = CharField(max_length=64)

    good_fors = Attraction.good_fors.copy()
    good_fors.remove('Adrenaline Seekers')
    tuple_choices = [(choice.lower().replace(' ', '_'), choice) for choice in good_fors]
    good_for = CharField(max_length=64, choices=tuple_choices)

    def get_absolute_url(self):
        return reverse("core:thing_detail", kwargs={"pk": self.pk})

class Picture(models.Model):
    thing = ForeignKey(Thing, on_delete=models.CASCADE, null=True)
    image = ImageField(upload_to='thing_pics')

    def get_absolute_url(self):
        return reverse(f"core:thing_detail", kwargs={"pk": self.thing.pk})