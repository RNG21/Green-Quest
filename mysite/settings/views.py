from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='/login')
def render_settings(request):
    return render(request, 'settings.html')


@login_required(login_url='/login')
def delete_account(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        if request.user.check_password(password):
            # delete account.
            request.user.delete()
            # logout the user
            logout(request)
            return redirect('/')
        else:
            # make label messages say invalid password
            messages.error(request, 'Invalid password, account not deleted.')
            return redirect('/settings')

    return redirect('/settings')


@login_required(login_url='/login/')
def logoutUser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    return redirect('home')


@login_required(login_url='/login/')
def changePassword(request):
    if request.method == 'POST':
        oldPassword = request.POST.get("oldPassword")
        newPassword = request.POST.get("newPassword")
        confirmPassword = request.POST.get("confirmPassword")
        if request.user.check_password(oldPassword):
            if oldPassword == newPassword:
                # send a message to the user that the new password is the same as the old password.
                messages.error(request, 'New password cannot be the same as the old password')
                return redirect('/settings')
            elif newPassword != confirmPassword:
                # not allowed either
                messages.error(request, 'Passwords do not match. Please try again.')
                return redirect('/settings')
            else:
                # change password and logout the user
                request.user.set_password(newPassword)
                request.user.save()
                logout(request)
                return redirect('/login')
        else:
            # incorrect password
            messages.error(request, 'Incorrect password, Password not changed.')
            return redirect('/settings')
    return redirect('/settings')
