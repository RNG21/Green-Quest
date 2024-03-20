from django.contrib import admin
from .models import Task, CompleteTask, TaskType, Location, Like, Profile

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'taskType', 'description', 'location')

@admin.register(CompleteTask)
class CompleteTaskAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'task', 'completion_date', 'description', 
                    'image', 'latitude', 'longtitude','score')

@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'taskName', 'description')

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'locationName', 'description',
                     'longtitude','latitude')

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id','CompleteTask', 'user',
                    'created')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','faculty')
# Register your models here.
