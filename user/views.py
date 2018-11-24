from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.contrib import messages

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.get(email=email)

        if user.check_password(password):
            login(request, user)

    return render(request, 'user/login.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if len(name.split(' ')) == 1:
            first_name = name.split(' ')[0]
            user = User.objects.create_user(username=first_name, first_name=first_name, email=email, password=password1)

        elif len(name.split(' ')) > 1:
            first_name = name.split(' ')[0]
            last_name = name.split(' ')[len(name.split(' '))-1]

            user = User.objects.create_user(username=first_name, first_name=first_name, last_name=last_name, email=email, password=password1)


        login(request, user)

    return render(request, 'user/register4.html')
