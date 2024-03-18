import sys

from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from django.core.wsgi import get_wsgi_application

# 设置Django环境
sys.path.append('/path/to/your/django/project')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project.settings")
application = get_wsgi_application()

from your_app.tasks import assign_daily_tasks  # 导入上面定义的函数

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")

    # 添加定时任务，每天午夜执行
    scheduler.add_job(
        assign_daily_tasks,
        'cron',
        hour=0,
        minute=0,
        id='daily_task_assignment',
        max_instances=1,
        replace_existing=True,
    )
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass

if __name__ == '__main__':
    start_scheduler()