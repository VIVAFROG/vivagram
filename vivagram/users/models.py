from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class User(AbstractUser):

    GENDER_CHOICES = {
        ('male', 'Male'),
        ('female', 'Female'),
        ('not-specified', 'Not specified')
    }

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)
    website = models.URLField(null=True)
    bio = models.TextField(null=True)
    phone = models.CharField(null=True, max_length=140)
    gender = models.CharField(null=True, max_length=80, choices=GENDER_CHOICES)
    followers = models.ManyToManyField("self")
    following = models.ManyToManyField("self")

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})