from django.contrib import admin
from .models import Country, Category, Check, Quality, Certificate, Product


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['id', 'country_name']
    list_display_links = ['country_name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    list_display_links = ['title']

    prepopulated_fields = {'slug': ['title']}


@admin.register(Check)
class CheckAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    list_display_links = ['title']


@admin.register(Quality)
class QualityAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    list_display_links = ['title']


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'certifier', 'certified_at']
    list_display_links = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'manufacturer']
    list_display_links = ['name']

    prepopulated_fields = {'slug': ['name', 'manufacturer']}

