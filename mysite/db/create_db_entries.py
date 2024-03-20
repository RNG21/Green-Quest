import traceback

from django.db.utils import IntegrityError
from django.db import models

from db.models import Location, TaskType, Task

def create_entries():
	task_types = [
		TaskType(taskName='Recycle'),
		TaskType(taskName='Use reusable items'),
		TaskType(taskName='Save energy!')
	]

	locations = [
		Location(locationName='XFI', latitude=50.735987, longtitude=-3.529907),
		Location(locationName='Forums', latitude=50.735274, longtitude=-3.533442),
		Location(locationName='Streatham Court', latitude=50.735784, longtitude=-3.530982),
		Location(locationName='Harrison', latitude=50.737704, longtitude=-3.532485),
		Location(locationName='Amory', latitude=50.736658, longtitude=-3.531870)
	]
	
	for obj in [*task_types, *locations]:
		try:
			obj.save()
		except IntegrityError:
			pass  # ignore

	[
		Task(taskType_id=taskType.id, location_id=location.locationName).save() 
		for location in locations for taskType in task_types
	]

	