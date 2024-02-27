from django.db import models
class User(models.Model):
    username = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.Username}, {self.Role}"

class TaskType(models.Model):
    typeID = models.AutoField(primary_key=True)
    taskName = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.typeID}, {self.taskName}"

class Task(models.Model):
    taskID = models.AutoField(primary_key=True)
    taskType = models.author = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    time = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.taskID}, {self.taskName}"

class UserTask(models.Model):
    userName = models.ForeignKey(User, on_delete=models.CASCADE)
    taskID = models.ForeignKey(Task, on_delete=models.CASCADE)
    time = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.userName}, {self.taskID}"
# Create your models here.
