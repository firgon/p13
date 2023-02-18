from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile')
    favorite_city = models.CharField(max_length=64, blank=True)
    objects = models.Manager()  # Only useful for pycharm developing

    def __str__(self):
        return self.user.username
