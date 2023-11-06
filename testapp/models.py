from django.db import models


# Create your models here.
class Member(models.Model):
    fullname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.fullname


class Product(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField(default=0)
    description = models.TextField()

    def __str__(self):
        return self.name
