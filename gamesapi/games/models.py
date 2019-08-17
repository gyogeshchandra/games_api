from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.

class Game(models.Model):
    title = models.CharField(max_length=255)
    genre = models.TextField()
    platform = models.TextField()
    score = models.FloatField()
    editors_choice = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}: {}".format(self.id, self.title)

    class Meta:
        ordering = ["-created"]
