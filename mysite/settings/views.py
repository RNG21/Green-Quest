# settings/views.py
from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def render_settings(request: HttpResponse):
    return render(request, 'settings.html')

def delete_account(request):
    if request.method == 'POST':
        # delete account

        request.user.delete()
        logout(request)

        return redirect('home')
    else:
        return render(request, 'settings.html')

