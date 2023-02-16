from django.contrib import admin

# Register your models here.
from .models import People, Item

admin.site.register(People)
admin.site.register(Item)
