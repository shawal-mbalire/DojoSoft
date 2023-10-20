from django.contrib import admin

# Register your models here.
from .models import User,Todo

admin.site.register(User)
admin.site.register(Todo)