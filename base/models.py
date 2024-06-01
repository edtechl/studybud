from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    # allow empty db value, allow empty form
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(
        User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)  # on every update
    created = models.DateTimeField(auto_now_add=True)  # only on creation

    # Model Meta (internal class): https://docs.djangoproject.com/en/5.0/ref/models/options/
    class Meta:
        # Reverse order (descending). For ascending order, remove the '-' prefix
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name


class Message(models.Model):
    # when a user is deleted, delete all messages for that user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # when a room is deleted, delete all messages in that room
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)  # on every update
    created = models.DateTimeField(auto_now_add=True)  # only on creation

    def __str__(self):
        return self.body[0:50]