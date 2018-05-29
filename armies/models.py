from django.db import models

default_max_length = 100


class Army(models.Model):
    polity = models.ForeignKey(
        'polity.Polity', on_delete=models.CASCADE,
        related_name='army', related_query_name='army'
    )
    name = models.CharField(max_length=default_max_length)

    def __str__(self):
        return "%s (%s)" % (self.name, self.polity.name)
