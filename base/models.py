from django.db import models
from django.contrib.auth.models import User

class Sportsman(models.Model):
    name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    parent_name = models.CharField(max_length=50)
    birthday = models.DateField()
    phone_number = models.CharField(max_length=12)
    address = models.CharField(max_length=300, null=True, blank=True)
    passport = models.CharField(max_length=20)
    photo = models.ImageField(null=True, blank=True, upload_to="sportmen-images/", verbose_name="Изображение")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
