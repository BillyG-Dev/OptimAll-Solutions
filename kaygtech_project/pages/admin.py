from django.contrib import admin
from .models import DeploymentBrief
# Register your models here.
@admin.register(DeploymentBrief)
class DeploymentBriefAdmin(admin.ModelAdmin):
    # What columns show up in your database dashboard grid
    list_display = ('name', 'email', 'service', 'created_at')
    
    # Quick filter panel on the right side for sorting requests
    list_filter = ('service', 'created_at')
    
    # Search bar parameters to scan client briefs quickly
    search_fields = ('name', 'email', 'message')
    
    # Sorts the most recent incoming client leads to the very top
    ordering = ('-created_at',)