from django.contrib import admin
from .models import Post
# Register your models here.
admin.site.register(Post)

#The admin.py file is only for connecting modles to the django built in admin-system