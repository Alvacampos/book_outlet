from operator import add
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Countries"

class Address(models.Model):
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.street}, {self.city}, {self.zip_code}'
    
    class Meta:
        verbose_name_plural = "Address Entries"

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, related_name='authors')
    
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def __str__(self):
        return self.full_name()

class Book(models.Model):
    title = models.CharField(max_length=200)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='books')
    is_bestseller = models.BooleanField(default=False)
    slug = models.SlugField(default='', blank=True, null=False, db_index=True)
    published_countries = models.ManyToManyField(Country, null=False, blank=True, related_name='books')
    
    def __str__(self):
        return f'Title: {self.title}, Rating: {self.rating}'
    
    def get_absolute_url(self):
        return reverse("book_detail", args=[self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_full_info(self):
        return f'Title: {self.title}, Rating: {self.rating}, Author: {self.author}, Bestseller: {self.is_bestseller}'
    
   