from django.db import models

# Create your models here.
# __str__ method is like toString method in Java.
# self is an instance of class, like 'this' in Java.
# the parameter of class is base class (=superclass) name,
# Category and Page are names of derived class (=subclass)
# that inherits the base class, which is models.Model.

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
