from django.db import models # type: ignore

# Create your models here.
class Library(models.Model):
    name = models.CharField(max_length=100)
    usn = models.CharField(max_length=20, unique=True)
    sem = models.IntegerField()
    branch = models.CharField(max_length=50)
    bookname = models.CharField(max_length=100)
    iSBInumber = models.IntegerField()
    authorname = models.CharField(max_length=100)

    def __str__(self):
        return self.name 