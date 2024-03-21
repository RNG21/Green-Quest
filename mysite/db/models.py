from django.db import models, transaction
from django.contrib.auth.models import User as U
from django.core.exceptions import ValidationError
from django.utils.timezone import now

class User(U):
    faculty = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return str(self.username)


class Location(models.Model):
    locationName = models.CharField(primary_key=True, max_length=100)
    description = models.CharField(max_length=100)
    longtitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    def __str__(self):
        return f"{self.locationName}"

class TaskType(models.Model):
    taskName = models.CharField(max_length=100, default = 'recycle')
    description = models.CharField(max_length=300, default='Default description')
    def __str__(self):
        return f" {self.taskName}"

class Task(models.Model):
    taskType = models.ForeignKey(TaskType, on_delete=models.CASCADE, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f'{self.location} - {self.taskType}'

class CompleteTask(models.Model):
    # The attribute that link Task and User, 
    # and define whether the task is done or not
    user = models.ForeignKey(U, on_delete=models.CASCADE, null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)
    completion_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    latitude = models.FloatField(null=True)
    longtitude = models.FloatField(null=True)
    score = models.IntegerField(default=0)
    showcase_image = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.user.username} - {self.task.taskType}'
    
    @transaction.atomic
    def save(self, *args, **kwargs):
        # get current date
        today = now().date()

        if kwargs.get("check_duplicate"):
            # Check if today the user did the same task before
            tasks_today = CompleteTask.objects.select_for_update().filter(
                user=self.user,
                task=self.task,
                completion_date__year=today.year, 
                completion_date__month=today.month, 
                completion_date__day=today.day
            )

            if tasks_today.exists():
                raise ValidationError("You cannot complete the same task more than once in a day.")
            del kwargs["check_duplicate"]
            
        super(CompleteTask, self).save(*args, **kwargs)


class Like(models.Model):
    CompleteTask = models.ForeignKey(CompleteTask, on_delete=models.CASCADE, related_name='like')
    user = models.ForeignKey(U, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.CompleteTask}{self.user}"
