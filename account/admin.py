from django.contrib import admin
from .models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display =  ['user', 'date_of_birth', 'photo']
    list_filter  =  ['user']
    search_fields = ['user']
    raw_id_fields = ['user']
