from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import CompleteTask, Task, TaskType

class CompleteTaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        task_type = TaskType.objects.create(taskName='Test Task')
        self.task = Task.objects.create(taskType=task_type)
        self.complete_task = CompleteTask.objects.create(user=self.user, task=self.task)

    def test_complete_task_str(self):
        self.assertEqual(str(self.complete_task), 'testuser -  Test Task')

    def test_complete_task_save(self):
        # Test saving a complete task
        task_type = TaskType.objects.create(taskName='New Task')
        new_task = Task.objects.create(taskType=task_type)
        new_complete_task = CompleteTask(user=self.user, task=new_task)
        new_complete_task.save()  # This should not raise an exception

    def tearDown(self):
        self.user.delete()
        self.task.delete()
        self.complete_task.delete()