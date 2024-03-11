from django.test import TestCase
from .models import TaskType
from .models import Location

class TaskTypeTestCase(TestCase):
    def setUp(self):
        self.location = Location.objects.create(
            locationName='Test Location',
            description='Test Description',
            longitude=0.0,
            latitude=0.0
        )
        self.task_type = TaskType.objects.create(
            taskName='Test Task',
            description='Test Description',
            location=self.location
        )

    def test_task_type_str(self):
        self.assertEqual(
            str(self.task_type),
            f"{self.task_type.typeID}, {self.task_type.taskName}"
        )

    def test_task_type_location(self):
        self.assertEqual(self.task_type.location, self.location)

    # Add more tests as needed