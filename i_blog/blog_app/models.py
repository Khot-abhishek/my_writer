from django.db import models
from django.utils.html import format_html
from tinymce.models import HTMLField
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/')
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def image_thumbnail(self):
        return format_html("<img src='/media/{}' style='width:40px; height:40px' >".format(self.image))

class Post(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = HTMLField()
    image = models.ImageField(upload_to='post/')
    url = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def image_thumbnail(self):
        return format_html("<img src='/media/{}' style='width:40px; height:40px' >".format(self.image))
    