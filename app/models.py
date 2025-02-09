from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=1, verbose_name="Сокращенное имя категории")
    full_name = models.CharField(max_length=50, verbose_name="Полное имя категории")

    def __str__(self):
        return f"{self.name} - {self.full_name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


# Create your models here.
class Car(models.Model):
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    date = models.DateField()
    description = models.TextField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, related_name="categories", on_delete=models.CASCADE)

    def __str__(self):
        return self.brand


