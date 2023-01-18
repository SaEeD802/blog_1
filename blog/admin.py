from django.contrib import admin
from . import models

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'about', 'created', 'date_modified']

admin.site.register(models.Post, PostAdmin)