from db.models import Location, TaskType, Task

task_types = [
	TaskType(taskName='Recycle'),
	TaskType(taskName='Use reusable items'),
	TaskType(taskName='Save energy!')
]
TaskType.objects.bulk_create(task_types)


locations = [
	Location(locationName='XFI', latitude=50.735987, longtitude=-3.529907),
	Location(locationName='Forums', latitude=50.735274, longtitude=-3.533442),
	Location(locationName='Streatham Court', latitude=50.735784, longtitude=-3.530982),
	Location(locationName='Harrison', latitude=50.737704, longtitude=-3.532485),
	Location(locationName='Amory', latitude=50.736658, longtitude=-3.531870)
]
Location.objects.bulk_create(locations)


tasks = [
	Task(taskType_id=taskType_id+1, location_id=location_id+1) for location_id in range(len(locations)) for taskType_id in range(len(task_types))
]
Task.objects.bulk_create(tasks)