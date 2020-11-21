from django.db import models


# Create your models here.

class Pet(models.Model):
    CAT = 'cat'
    DOG = 'dog'
    PARROT = 'parrot'

    type_animal = [
        (CAT, 'cat'),
        (DOG, 'dog'),
        (PARROT, 'parrot'),

    ]
    type = models.CharField(max_length=6, choices=type_animal)
    name = models.CharField(max_length=6)
    age = models.PositiveIntegerField()
    description = models.TextField()
    images = models.ImageField(upload_to='images')


class Like(models.Model):
    like = models.ForeignKey(Pet, on_delete=models.CASCADE)
    test = models.CharField(max_length=2)


class Comments(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
