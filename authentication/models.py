from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    profile_photo = models.ImageField(verbose_name='Photo de profile')
    bio = models.TextField(blank=True)

    follows = models.ManyToManyField('self',
                                     related_name="followed_by",
                                     symmetrical=False,
                                     blank=True)

    def __str__(self):
        return self.username

    def add_follow(self, user):
        self.follows.add(user)

    def delete_follow(self, user):
        self.follows.remove(user)

    def is_following(self, user):
        return self.follows.filter(id=user.id).exists()
