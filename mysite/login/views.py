from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect

from db.models import User

# Create your views here.
def index(request):
    return render(request,'index.html',locals())


def logins(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            return redirect('/')
        else:
            msg='Incorrect Password!'
            return render(request,'login.html',locals())
    return render(request,'login.html')


def register(request):
    if request.method == 'POST':
        faculty = request.POST.get('faculty')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        if password != password2:
            msg='The passwords entered do not match!'
            return render(request,'register.html',locals())
        elif username == '':
            msg='Username cannot be empty!'
            return render(request,'register.html',locals())
        if User.objects.filter(username=username).exists():
            msg='Username already exists. Please Choose a different one.'
            return render(request,'register.html',locals())
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(faculty=faculty, username=username, password=password, email=email)
            return redirect('/login/')
    return render(request,'register.html')


def log_out(request):
    logout(request)
    return redirect('/')
