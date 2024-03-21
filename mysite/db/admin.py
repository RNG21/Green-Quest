from django.contrib import admin
from .models import Task, CompleteTask, TaskType, Location, Like, User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "faculty", "email", "date_joined")

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'taskType', 'description', 'location')

@admin.register(CompleteTask)
class CompleteTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'task', 'completion_date', 'description', 
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

# Register your models here.
