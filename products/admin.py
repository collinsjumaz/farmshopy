from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
# Register your models here.
admin.site.register(Product)
