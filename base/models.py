from django.db import models


# Create your models here.
class Student(models.Model):
    id = models.BigAutoField(primary_key=True)
    sName = models.CharField(max_length=20)
    age = models.FloatField()
    image = models.ImageField(null=True,blank=True,default="/placeholder.png")

    def __str__(self):
        return self.sName