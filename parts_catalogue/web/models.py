from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Part(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image_link = models.URLField()
    comment = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    available = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
