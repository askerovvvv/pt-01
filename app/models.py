from django.db import models


# Create your models here.
class Car(models.Model):
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    date = models.DateField()
    description = models.TextField()
    price = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.brand


