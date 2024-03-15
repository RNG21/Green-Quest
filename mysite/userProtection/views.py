from django.shortcuts import render


# Create your views here.
def render_userProtection(request):
    return render(request, 'userProtection.html')
