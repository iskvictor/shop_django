from django.db import models
from django.urls import reverse

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=52)
    describe = models.TextField()
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    year = models.IntegerField()
    photo = models.ImageField(upload_to='images')
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.title




class Author(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=40, unique=True)
    slug = models.SlugField(max_length=50, null=True)

    def __str__(self):
        return self.name



    #def get_absolute_url(self):
        #return reverse('post', kwargs={'slug': self.slug, 'id': self.id})


