from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = 'myapp'

    def ready(self):
        from .auto_task import start_scheduler  # 假设scheduler.py包含了start_scheduler函数
        start_scheduler()

class ChallengesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'challenges'
