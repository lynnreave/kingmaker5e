from django.db import models

default_max_length = 100

# Create your models here.


class Gender(models.Model):
    name = models.CharField(max_length=default_max_length)

    def __str__(self):
        return self.name


class NobleRank(models.Model):
    name = models.CharField(max_length=default_max_length)
    equivalence = models.CharField(max_length=default_max_length)
    honorific = models.CharField(max_length=default_max_length)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField(max_length=default_max_length)
    middle_name = models.CharField(max_length=default_max_length, blank=True)
    last_name = models.CharField(max_length=default_max_length)
    gender = models.OneToOneField(Gender, on_delete=models.CASCADE)
    noble_rank = models.OneToOneField(NobleRank, on_delete=models.CASCADE, blank=True, null=True)
    #awards = models.ManyToManyField(Award, blank=True, related_name='persons', related_query_name='person')
    str = models.IntegerField(default=10)
    dex = models.IntegerField(default=10)
    con = models.IntegerField(default=10)
    int = models.IntegerField(default=10)
    wis = models.IntegerField(default=10)
    cha = models.IntegerField(default=10)
    notes = models.TextField(blank=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Award(models.Model):
    name = models.CharField(max_length=default_max_length)
    desc = models.TextField(blank=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='awards', related_query_name='award', blank=True, null=True)

    def __str__(self):
        return self.name
