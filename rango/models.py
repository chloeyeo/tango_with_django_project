from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
# __str__ method is like toString method in Java.
# self is an instance of class, like 'this' in Java.
# the parameter of class is base class (=superclass) name,
# Category and Page are names of derived class (=subclass)
# that inherits the base class, which is models.Model.

class Category(models.Model):
    NAME_MAX_LENGTH = 128
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Page(models.Model):
    
    TITLE_MAX_LENGTH = 128
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    # one to one relationship between User model instance and UserProfile.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # The additional attributes we wish to include to the User model:
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
