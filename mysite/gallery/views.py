import json

from django.shortcuts import render
from django.http import HttpRequest, JsonResponse

from db.models import CompleteTask, Like

def render_gallery(request: HttpRequest):
    # Respond to post request
    body = request.body.decode('utf-8')
    if request.method=="POST" and request.user.is_authenticated:

        body = json.loads(body)
        c_task_id = body["like"]
        user_id = request.user.id

        total_likes = Like.objects.filter(CompleteTask=c_task_id)
        this_usr_like = total_likes.filter(user=user_id)
        total_likes = len(total_likes)
        if not this_usr_like:
            Like(CompleteTask=CompleteTask.objects.get(id=c_task_id), user=request.user).save()
            total_likes += 1
            is_liked = True
        else:
            this_usr_like.delete()
            total_likes -= 1
            is_liked = False
        return JsonResponse({"total_likes": total_likes, "is_liked": is_liked, "status": "ok"})


    completed_tasks = [task for task in CompleteTask.objects.all() if task.showcase_image]

    context = {
        "tasks": completed_tasks
    }

    return render(request, "gallery/gallery.html", context=context)
