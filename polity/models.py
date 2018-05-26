from django.db import models

default_max_length = 100


class Polity(models.Model):
    name = models.CharField(max_length=default_max_length)
    desc = models.TextField(default="", blank=True)

    def __str__(self):
        return self.name
