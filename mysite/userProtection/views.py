from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def render_userProtection(request):
    admin = User.objects.filter(is_staff=True).first()
    return render(request, 'userProtection.html',context={"admin_email": admin.email})
