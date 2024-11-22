from django.db import models

class Cat(models.Model):
    name = models.CharField(max_length=50, null=False)
    age = models.PositiveIntegerField(null=False)
    year_of_exp = models.PositiveIntegerField(null=False)
    breed = models.CharField(max_length=100, null=False)
    salary = models.PositiveIntegerField(default=0)

class Target(models.Model):
    name = models.CharField(max_length=50, null=False)
    country = models.CharField(max_length=100, null=False)
    state = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)

class Mission(models.Model):
    name = models.CharField(max_length=300, null=False)
    targets = models.ManyToManyField(Target)
    assigned_cat = models.OneToOneField(Cat,on_delete=models.SET_NULL, null=True)
    completed = models.BooleanField(default=False)
    