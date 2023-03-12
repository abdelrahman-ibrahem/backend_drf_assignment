from django.contrib import admin
from .models import Task

class CustomoTaskAdminView(admin.ModelAdmin):
    list_display = [
        'user',
        'title',
        'due_date',
        'completed'
    ]
admin.site.register(Task, CustomoTaskAdminView)