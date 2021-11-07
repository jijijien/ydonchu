from django.contrib import admin
from .models import People,What_food


class PostAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'how_many', 'point']
    
admin.site.register(People, PostAdmin)
admin.site.register(What_food)