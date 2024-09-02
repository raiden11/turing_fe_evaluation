
from django.contrib import admin
from .models import Campaign, Member, Task

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['email', 'full_name', 'role', 'created_at', 'updated_at']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'score', 'campaign', 'trainer', 'lead', 'created_at', 'updated_at']
