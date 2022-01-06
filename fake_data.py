import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mg_tourism.settings')

import django
django.setup()

from core.models import Thing, Attraction, Tour, Picture
from django.core.files import File
from faker import Faker

import datetime
import requests
import shutil
import random

f = Faker('pt_BR')
fus = Faker('en_US')

def populate(N=5):
    categories = {'Attraction': create_attraction,
        'Tour': create_tour}

    for _ in range(N):
        for category in categories:
            thing = create_thing(category)
            place = categories[category](thing)
            picture = create_picture(place)
            picture2 = create_picture(place)
            picture3 = create_picture(place)

            place.save()
            picture.save()
            picture2.save()
            picture3.save()

def create_attraction(thing):
    type_ = random.choice(
        [choice[1] for choice in Attraction._meta.get_field('type').choices])
    
    neighborhood = random.choice(['Santa Inês','Jardim São José',
        'Vila Betânia', 'Dom Bosco',
        'Jonas Veiga', 'Bacurau',
        'São Francisco', 'Nossa Senhora Do Rosário',
        'Santa Monica', 'Paraíso'])
    
    good_for = random.choice(
        [choice[1] for choice in Attraction._meta.get_field('good_for').choices])

    attraction = Attraction.objects.get_or_create(
        name=thing[0],
        long_description=thing[1],
        short_description=thing[2],
        address=thing[3],
        stars=thing[4],
        category=thing[5],
        covid_safe=thing[6],
        type=type_,
        neighborhood=neighborhood,
        good_for=good_for)[0]

    return attraction

def create_tour(thing):
    t = random.choice(
        [choice[1] for choice in Tour._meta.get_field('type').choices])

    price = random.randint(10, 500)
    duration = datetime.timedelta(seconds=random.choice([3600*i for i in range(30)]))

    tour = Tour.objects.get_or_create(
        name=thing[0],
        long_description=thing[1],
        short_description=thing[2],
        address=thing[3],
        stars=thing[4],
        category=thing[5],
        covid_safe=thing[6],
        type=t,
        price=price,
        duration=duration)[0]

    return tour

def create_thing(category):
    name = f"{f.city()} {f.company()}"
    long_description = fus.paragraph(nb_sentences=12, variable_nb_sentences=False)
    short_description = fus.paragraph(nb_sentences=3, variable_nb_sentences=False)
    address = get_address()
    stars = random.randint(2, 5)
    category = category
    covid_safe = random.choice([True, False])

    thing = (name,
        long_description,
        short_description,
        address,
        stars,
        category,
        covid_safe)

    return thing

def get_address():
    while True:
        add = f.address()
        if add[-2:] == 'MG':
            return add.replace('\n', ' ')

def create_picture(thing):
    get_image()
    picture = Picture.objects.get_or_create(
        thing=thing,
        image=File(open('img.jpg', 'rb')))[0]

    return picture

def get_image(filename='img.jpg',
    url='https://picsum.photos/1280/720'):

    r = requests.get(url, stream = True)

    if r.status_code == 200:
        r.raw.decode_content = True
        
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)

if __name__ == "__main__":
    print("populatin script ran")
    populate(N=6)
    print("population complete")