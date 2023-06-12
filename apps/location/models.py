import imghdr
from unicodedata import category
from django.db import models
from slugify import slugify

from django.contrib.auth import get_user_model

# from apps.business.models import BusinessProfile, Guide
from datetime import datetime

current = str(datetime.now())


User = get_user_model()

class Location(models.Model):

    CATEGORY_CHOICES = (
        ('easy', 'легкий'),  ## change
        ('medium', 'средний'), ##
        ('hard', 'сложный') ##
    )

    title = models.CharField(max_length=100, verbose_name='Название тура')
    slug = models.SlugField(max_length=120, primary_key=True, blank=True)
    description = models.CharField(max_length=150) # text field

    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='Юзер',
        related_name='locations',
    )
    image = models.ImageField(upload_to='media/tour_image', blank=True)  # change folders
    category = models.ManyToManyField(
        to='Category', ## is that right
        related_name='categories',
        # blank=True
    )
    map_coordinates = models.CharField() ##

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:  
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'


class LocationImage(models.Model):
    image = models.ImageField(upload_to='location_images/carousel')
    post = models.ForeignKey(
        to=Location,
        on_delete=models.CASCADE,
        related_name='location_images'
    )


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(primary_key=True, blank=True, max_length=35)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title) # + str(self.created_at)
        return super().save(*args, **kwargs)