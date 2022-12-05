from django.contrib import admin
from django.db.models import Count

from . import models


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'name', 'profession']
    list_filter = ['profession']


class ProfessionAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'title_url': ['title']
    }


admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Profession, ProfessionAdmin)
