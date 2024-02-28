from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.username}, {self.role}"

class Location(models.Model):
    locationName = models.CharField(primary_key=True, max_length=100)
    description = models.CharField(max_length=100)
    longitude = models.FloatField()
    latitude = models.FloatField()

class TaskType(models.Model):
    typeID = models.AutoField(primary_key=True)
    taskName = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.typeID}, {self.taskName}"

class Task(models.Model):
    taskID = models.AutoField(primary_key=True)
    taskType = models.author = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    time = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.taskID}, {self.taskType}"

class UserTask(models.Model):
    userName = models.ForeignKey(User, on_delete=models.CASCADE)
    taskID = models.ForeignKey(Task, on_delete=models.CASCADE)
    time = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.userName}, {self.taskID}"
