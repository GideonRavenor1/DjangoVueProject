from django.db import models
from django.contrib.auth.models import AbstractUser


class Permission(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return '%s' % self.name


class Role(models.Model):
    name = models.CharField(max_length=200)
    permissions = models.ManyToManyField(Permission)

    def __str__(self):
        return '%s' % self.name


class User(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, related_name="user")

    class Meta:
        ordering = ['date_joined']



