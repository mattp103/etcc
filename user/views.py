from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.contrib import messages

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.get(username=username)

        if user.check_password(password):
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')

        return redirect('index')

    return render(request, 'user/login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        name = request.POST.get('name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if len(User.objects.filter(username=username)) == 0 and len(User.objects.filter(email=email)) == 0 and password1 == password2:

            if len(name.split(' ')) == 1:
                first_name = name.split(' ')[0]
                user = User.objects.create_user(username=username, first_name=first_name, email=email, password=password1)

            elif len(name.split(' ')) > 1:
                first_name = name.split(' ')[0]
                last_name = name.split(' ')[len(name.split(' '))-1]

                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password1)


            login(request, user, backend='django.contrib.auth.backends.ModelBackend')

            for reading in Reading.objects.all():
                Progress.objects.create(usr=user, reading=reading, status=False)

            return redirect('index')

        else:
            messages.error(request, "Error. Please make sure all the fields are filled in and valid.")

    return render(request, 'user/register.html')

def signout(request):
    logout(request)
    return render(request, "user/logout.html")



def delete(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('index')
        messages.success(request, 'Account deleted')

    return render(request, 'user/delete.html')
