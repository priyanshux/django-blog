from django.contrib import admin

# Importing Post from models.
from .models import Post
admin.site.register(Post)