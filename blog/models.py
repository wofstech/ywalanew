from django.db import models
from datetime import datetime


class Post(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()
    time = models.DateTimeField(default = datetime.now, blank = True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ["-time"]