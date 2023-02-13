from django.contrib import admin
from .models import *

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    search_fields=('name',)
    list_display=['category','subcategory','name']
    list_filter=['category','subcategory']


class SubCategoryAdmin(admin.ModelAdmin):
    search_fields=('name',)
    list_display=['name']


class CategoryAdmin(admin.ModelAdmin):
    search_fields=('name',)
    list_display=['name']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(SubCategory,SubCategoryAdmin)