from django.urls import reverse

from django.db.models.fields import CharField, DurationField, SmallIntegerField

from .thing import Thing

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

class Tour(Thing):
    category = 'Tour'

    types = ['Multi-day', 'City', 'Cultural', 'Historical', 'Private']
    tuple_types = [(t.lower().replace(' ', '_'), t) for t in types]
    type = CharField(max_length=64, choices=tuple_types)

    price = SmallIntegerField()
    duration = DurationField()

    def get_absolute_url(self):
        return reverse("core:thing_detail", kwargs={"pk": self.pk})

class Food(Thing):
    types = ['Farmers Market', 'Breweries and Wine', 'Coffee Shop', 'Restaurant', 'Bar']
    tuple_types = [(t.lower().replace(' ', '_'), t) for t in types]
    type = CharField(max_length=64, choices=tuple_types)

    neighborhood = CharField(max_length=64)

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