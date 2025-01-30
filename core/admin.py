from django.contrib import admin
from core.models import Person

@admin.register(Person)
class PersonModel(admin.ModelAdmin):
    list_display = ['name','address']

# Register your models here.
