from datetime import date
from statistics import mean

from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

from django.db.models.fields import BooleanField, CharField, DateField, SmallIntegerField, TextField
from django.db.models.fields.related import ForeignKey

from .thing import Thing
from .user import UserProfile

class Review(models.Model):
    title = CharField(max_length=128)
    content = TextField(max_length=4096)
    rating = SmallIntegerField(validators=[MaxValueValidator(limit_value=5), MinValueValidator(limit_value=1)])    
    posted_on = DateField(default=timezone.now)
    is_edited = BooleanField(default=False)

    thing = ForeignKey(Thing, on_delete=models.CASCADE, related_name="reviews")
    author = ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="reviews")

    def save(self, *args, **kwargs) -> None:
        """Updates the average rating of a Thing when a new review is created"""

        if Review.objects.filter(pk=self.pk).exists():
            average = mean([getattr(review, 'rating') for review in self.thing.reviews.exclude(pk=self.pk)] + [self.rating])

        else:
            average = mean([getattr(review, 'rating') for review in self.thing.reviews.all()] + [self.rating])
        
        self.thing.stars = average
        self.thing.save()

        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(f"core:thing_detail", kwargs={"pk": self.thing.pk})