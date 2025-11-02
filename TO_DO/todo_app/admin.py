from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed', 'due_date', 'due_time', 'created_at')
    list_filter = ('completed',)
    search_fields = ('title', 'description')
    ordering = ('-created_at',)
