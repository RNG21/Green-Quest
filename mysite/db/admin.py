from django.contrib import admin
from .models import Task, UserTask

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'latitude', 'longitude')

@admin.register(UserTask)
class UserTaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'task', 'completed', 'completion_date')
    list_filter = ('completed', 'user')
# Register your models here.
