"""Generates fake data for the database"""

import pathlib
import os
from typing import Any, Dict, Tuple
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mg_tourism.settings')

import django
django.setup()

from core.models import (Thing,
    Tour, Attraction, Food, Outdoor, Shopping,
    Picture, UserProfile, Review, Plan)

from django.core.files import File
from faker import Faker

import datetime
import requests
import shutil
import random

PATH = pathlib.Path().resolve()

class FakeThingGenerator:

    neighborhoods = ['Santa Inês','Jardim São José',
        'Vila Betânia', 'Dom Bosco',
        'Jonas Veiga', 'Bacurau',
        'São Francisco', 'Nossa Senhora Do Rosário',
        'Santa Monica', 'Paraíso']

    def __init__(self, N=60):
        self.N = N

    def generate(self) -> None:
        """Generates N Thing objects of a randomly chosen category"""

        for _ in range(self.N):
            category = random.choice(list(categories.keys()))

            thing_fields = FakeThingGenerator.generate_thing_fields(category)
            category_fields = categories[category]()
            
            kwargs = thing_fields | category_fields
            thing = eval(f'{category}.objects.get_or_create(**kwargs)[0]')
            thing.save()
            
            FakeThingGenerator.add_pics(thing)

    @staticmethod
    def generate_thing_fields(category,
        long_description_length: int = 12,
        short_description_length: int = 3) -> Dict[str, Any]:
        
        """Generates random values for the fields of a Thing object"""

        name = f"{f_br.city()} {f_br.company()}"
        long_description = f_us.paragraph(nb_sentences=long_description_length,
            variable_nb_sentences=False)
        
        short_description = f_us.paragraph(nb_sentences=short_description_length,
            variable_nb_sentences=False)
        
        address = FakeThingGenerator.get_address()
        category = category
        covid_safe = random.choice([True, False])

        return {'name': name,
            'short_description': short_description,
            'long_description': long_description,
            'address': address,
            'category': category,
            'covid_safe': covid_safe}

    @staticmethod
    def generate_tour_specific_fields(min_price: int = 10,
        max_price: int = 500,
        min_duration: int = 2,
        max_duration: int = 30) -> Dict[str, Any]:
        
        """Generates random values for the fields specific to a Tour object"""

        type_ = random.choice(FakeThingGenerator.get_choices(Tour._meta.get_field('type')))
        price = random.randint(min_price, max_price)
        duration = datetime.timedelta(
            seconds=random.choice([3600*i for i in range(min_duration, max_duration)]))

        return {'type': type_,
            'price': price,
            'duration': duration}

    @staticmethod
    def generate_attraction_specific_fields() -> Dict[str, Any]:
        type_ = random.choice(FakeThingGenerator.get_choices(Attraction._meta.get_field('type')))
        neighborhood = random.choice(FakeThingGenerator.neighborhoods)
        good_for = random.choice(FakeThingGenerator.get_choices(Attraction._meta.get_field('good_for')))

        """Generates random values for the fields specific to an Attraction object"""

        return {'type': type_,
            'neighborhood': neighborhood,
            'good_for': good_for}

    @staticmethod
    def generate_food_specific_fields() -> Dict[str, Any]:
        """Generates random values for the fields specific to a Food object"""

        type_ = random.choice(FakeThingGenerator.get_choices(Food._meta.get_field('type')))
        neighborhood = random.choice(FakeThingGenerator.neighborhoods)
        good_for = random.choice(FakeThingGenerator.get_choices(Food._meta.get_field('good_for')))

        return {'type': type_,
            'neighborhood': neighborhood,
            'good_for': good_for}

    @staticmethod
    def generate_outdoor_specific_fields() -> Dict[str, Any]:
        """Generates random values for the fields specific to an Outdoor object"""

        type_ = random.choice(FakeThingGenerator.get_choices(Outdoor._meta.get_field('type')))
        neighborhood = random.choice(FakeThingGenerator.neighborhoods)
        good_for = random.choice(FakeThingGenerator.get_choices(Outdoor._meta.get_field('good_for')))

        return {'type': type_,
            'neighborhood': neighborhood,
            'good_for': good_for}

    @staticmethod
    def generate_shopping_specific_fields() -> Dict[str, Any]:
        """Generates random values for the fields specific to a Shopping object"""
        
        type_ = random.choice(FakeThingGenerator.get_choices(Shopping._meta.get_field('type')))
        neighborhood = random.choice(FakeThingGenerator.neighborhoods)
        good_for = random.choice(FakeThingGenerator.get_choices(Shopping._meta.get_field('good_for')))

        return {'type': type_,
            'neighborhood': neighborhood,
            'good_for': good_for}
            
    @staticmethod
    def get_choices(field: str) -> Tuple[str]:
        """Gets the possible choices for a field in a Thing or Thing children objects"""

        return [choice[1] for choice in field.choices]

    @staticmethod
    def get_address() -> str:
        """Returns a fake address in the state of Minas Gerais, Brazil"""
        while True:
            address = f_br.address()
            if address[-2:] == 'MG':
                return address.replace('\n', ' ')

    @staticmethod
    def add_pics(thing: Thing, N: int = random.randint(0, 3)) -> None:
        """Adds a random number of pictures to a Thing child object"""

        for _ in range(N):
            FakeThingGenerator.download_thing_pic()
            picture = Picture.objects.get_or_create(
                thing=thing,
                image=File(open('img.jpg', 'rb')))[0]

            picture.save()

    @staticmethod
    def download_thing_pic(filename: str = 'img.jpg',
        url: str = 'https://picsum.photos/1280/720') -> None:

        """Downloads a random image"""

        r = requests.get(url, stream = True)
        if r.status_code == 200:
            r.raw.decode_content = True
            with open(filename,'wb') as f:
                shutil.copyfileobj(r.raw, f)

class FakeUserGenerator:
    def __init__(self, profile_pics_path=PATH/'fake_profile_pics'):
        self.profile_pics_path = profile_pics_path

    def generate(self) -> None:
        """Generates a user for every profile picture in the profile_pics_path path"""
        
        for picture in os.listdir(self.profile_pics_path):
            FakeUserGenerator.create(f'fake_profile_pics/{picture}')

    @staticmethod
    def create(picture: str, biography_length: int = 7) -> None:
        """Creates a fake UserProfile object"""
        
        f_name = f_us.first_name()
        l_name = f_us.last_name()
        u_name = f_name.lower()[0]+l_name.lower() + str(random.randint(100, 999))
        email = u_name+"@"+"example.com"
        
        user = UserProfile.objects.get_or_create(username=u_name,
            first_name=f_name,
            last_name=l_name,
            email=email,
            password=str(random.randint(10000000, 99999999)),
            biography=f_us.paragraph(nb_sentences=biography_length),
            profile_pic=File(open(picture, 'rb')),
            )[0]

        user.save()

class FakeReviewGenerator:
    def __init__(self, users):
        self.users = users

    def generate(self) -> None:
        """Generates fake reviews for every user"""

        for user in self.users:
            FakeReviewGenerator.create(user)

    @staticmethod
    def create(user: UserProfile, max_n: int = 5) -> None:
        """Creates a random amount of fake reviews on unique things"""

        n = random.randint(1, max_n)
        things = random.choices(Thing.objects.all(), k=n)
        for thing in things:
            title = f_us.paragraph(nb_sentences=1, variable_nb_sentences=False)
            content = f_us.paragraph(nb_sentences=24)
            rating = random.randint(1, 5)

            review = Review.objects.get_or_create(title=title,
                content=content,
                rating=rating,
                thing=thing,
                author=user,
                is_edited=random.choice([False, False, True]),
                posted_on=datetime.date(year=2020, month=1, day=1) + datetime.timedelta(days=random.randint(0, 741)))[0]

            review.save()

class FakePlanGenerator:
    def __init__(self, users):
        self.users = users

    def generate(self) -> None:
        """Generates fake plans for each user"""

        for user in self.users:
            self.create(user)

    @staticmethod
    def create(user: UserProfile, max_n: int = 5, description_length: int = 7) -> None:
        """Creates a random amount of plans"""

        n = random.randint(0, max_n)
        for _ in range(n):
            plan = Plan.objects.get_or_create(
                name=f_us.paragraph(nb_sentences=1),
                description=f_us.paragraph(nb_sentences=description_length),
                is_public=True,
                owner=user)[0]

            plan.save()

            FakePlanGenerator.add_things(plan)
            FakePlanGenerator.add_favorites(plan)

    @staticmethod
    def add_things(plan: Plan, max_n: int = 5) -> None:
        """Adds a random amount of unique Thing objects to a plan"""

        n = random.randint(0, max_n)
        for thing in random.choices(Thing.objects.all(), k=n):
            plan.things.add(thing)

    @staticmethod
    def add_favorites(plan: Plan, max_n: int = 30) -> None:
        """Adds a random number of UserProfile objects to a plan's favorited_by attribute"""

        n = random.randint(0, max_n)
        for thing in random.choices(UserProfile.objects.all(), k=n):
            plan.favorited_by.add(thing)

f_br = Faker('pt_BR')
f_us = Faker('en_US')

categories = {'Tour': FakeThingGenerator.generate_tour_specific_fields,
    'Attraction': FakeThingGenerator.generate_attraction_specific_fields,
    'Food': FakeThingGenerator.generate_food_specific_fields, 
    'Outdoor': FakeThingGenerator.generate_outdoor_specific_fields,
    'Shopping': FakeThingGenerator.generate_shopping_specific_fields}

if __name__ == "__main__":
    print("Started populating.")
    
    FakeThingGenerator(N=20).generate()
    FakeUserGenerator().generate()
    FakeReviewGenerator(UserProfile.objects.all()).generate()
    FakePlanGenerator(UserProfile.objects.all()).generate()
    
    print("Finished populating.")