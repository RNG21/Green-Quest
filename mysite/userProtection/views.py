from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse

# Create your views here.
def render_userProtection(request):
    back_url = request.GET.get('back', None)
    if back_url is None:
        back_url = reverse("settings")
    else:
        back_url = reverse(back_url)

    context = {
        "admin_email": User.objects.filter(is_staff=True).first().email,
        "back_url": back_url
    }
    return render(request, 'userProtection.html', context=context)
