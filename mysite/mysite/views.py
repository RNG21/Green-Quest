#Author: Fred Westhead
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from db.models import CompleteTask
# Can add more views here. I think these are all the ones the navbar links to ? 
def home(request):
    return render(request, 'home.html')
def base(request):
    return render(request, 'mysite/base.html')
def settings(request):
    return render(request, 'settings.html')
def leaderboard(request):
    return render(request, 'leaderboard.html')
def challenges(request):
    return render(request, 'challenges.html')
def login(request):
    return render(request, 'login.html')
    
def gallery_view(request):
    tasks = CompleteTask.objects.all()
    return render(request, 'gallery.html',{'tasks':tasks} )

def like_image(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        task = CompleteTask.objects.get(id=task_id)

        if task.like.filter(user=request.user).exists():
            task.like.filter(user=request.user).delete()
            is_liked = False
        else:
            task.like.create(user=request.user, CompleteTask=task)
            is_liked = True
        
        return JsonResponse({'total_likes':task.total_likes(), 'is_liked': is_liked})
    