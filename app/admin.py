from django.contrib import admin
from .models import TravelPost
# Register your models here.

@admin.register(TravelPost)
class TravelPostAdmin(admin.ModelAdmin):
    list_display = ['picture','title','description','created_at']
    
