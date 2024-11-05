from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created', 'updated')
    list_display_links = ('title', 'slug', 'created', 'updated')
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'description', 'price', 'massa', 'count', 'rating', 'status', 'created', 'updated')
    list_display_links = ('id', 'title', 'slug', 'description', 'price', 'massa', 'count', 'rating', 'status', 'created', 'updated')
    list_filter = ('category', 'status', 'created', 'updated')
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    autocomplete_fields = ('category',)