from django.db import models
from django.utils import timezone
from .helpers import StatusChoices, MassaChoices

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=120)
    image = models.ImageField(upload_to='products/category/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True, null=False, blank=False)
    image = models.ImageField(upload_to='products/product/')
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    massa = models.CharField(max_length=4, choices=MassaChoices.choices, default=MassaChoices.KG)
    count = models.PositiveIntegerField(default=1)
    rating = models.FloatField(default=0, null=True, blank=True)
    status = models.CharField(max_length=10, choices=StatusChoices.choices, default=StatusChoices.PUBLISH)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @staticmethod
    def get_queryset():
        return Product.objects.all().order_by('id')

    # class Meta:
    #     ordering = ['id']

    def get_description_20item(self):
        return self.description[:20]

    def __str__(self):
        return self.title