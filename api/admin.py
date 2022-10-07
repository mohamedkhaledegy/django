from django.contrib import admin
from .models import Task
# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description','created_by','fix_by']
    search_fields = ['title', 'description','created_by']
    list_filter = ['title', 'description']
    
admin.site.register(Task,TaskAdmin)