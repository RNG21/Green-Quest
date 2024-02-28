from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/login')
def render_settings(request):
    return render(request, 'settings.html')


@login_required(login_url='/login')
def delete_account(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        if request.user.check_password(password):
            # delete account
            request.user.delete()
            # logout the user
            logout(request)

            return redirect('home')
        else:
            return render(request, 'settings.html')

    return render(request, 'settings.html')


@login_required(login_url='/login/')
def logoutUser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    return redirect('home')
