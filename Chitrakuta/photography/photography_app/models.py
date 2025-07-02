from django.db import models

# Create your models here.
class Authentication(models.Model):
    id = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.TextField()
    password = models.CharField()

    def __str__(self):
        return self.name
