from django.contrib import admin
from .models import Task, CompleteTask, TaskType, Location, Like

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'taskType', 'description', 'location')

@admin.register(CompleteTask)
class CompleteTaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'task', 'completion_date', 'description', 
                    'image', 'latitude', 'longtitude','score')

@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ('taskName', 'description')

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('locationName', 'description',
                     'longtitude','latitude')

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('CompleteTask', 'user',
                    'created')

# Register your models here.
