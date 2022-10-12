from django.contrib import admin
from .models import Category, Post

# Register your models here.
@admin.register(Category)
class CategoryAdminModel(admin.ModelAdmin):
    list_display = ['image_thumbnail','title', 'description', 'created']
    search_fields = ['title']
    
    
@admin.register(Post)
class PostAdminModel(admin.ModelAdmin):
    list_display = ['image_thumbnail','title', 'created_on']
    search_fields = ['title']