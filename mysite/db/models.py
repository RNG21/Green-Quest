from django.db import models
from django.contrib.auth.models import User as U

class User(U):
    faculty = models.CharField(max_length=100)
    def __str__(self):
        return str(self.username)

class Location(models.Model):
    locationName = models.CharField(max_length=100)
    description = models.CharField(max_length=100, default='Default description')
    longtitude = models.FloatField(default=1)
    latitude = models.FloatField(default=1)
    def __str__(self):
        return f" {self.locationName}"

class TaskType(models.Model):
    taskName = models.CharField(max_length=100, default = 'recycle')
    description = models.CharField(max_length=100, default='Default description')
    def __str__(self):
        return f" {self.taskName}"

class Task(models.Model):
    title = models.CharField(max_length=255, default='Untitled Task')
    taskType = models.ForeignKey(TaskType, on_delete=models.CASCADE, null=True)
    description = models.TextField(default='Default description')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.title

class CompleteTask(models.Model):
    # The attribute that link Task and User, 
    # and define whether the task is done or not
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)
    completion_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(default='Default description')
    image = models.ImageField(upload_to='images/')
    latitude = models.FloatField(default=1)
    longtitude = models.FloatField(default=1)
    score = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.user.username} - {self.task.title}'

class Like(models.Model):
    CompleteTask = models.ForeignKey(CompleteTask, on_delete=models.CASCADE, related_name='like')
    user = models.ForeignKey(U, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.CompleteTask}{self.user}"
    
    @staticmethod
    def filter(task, user):
        return Like.objects.filter(CompleteTask=task, user=user)