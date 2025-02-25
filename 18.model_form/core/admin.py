from django.contrib import admin
from .models import MarvelModel, DcModel
# Register your models here.

@admin.register(MarvelModel)
class MarvelAdmin(admin.ModelAdmin):
    list_display =['id','name','heroic_name']


@admin.register(DcModel)
class MarvelAdmin(admin.ModelAdmin):
    list_display =['id','name','heroic_name']