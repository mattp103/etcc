from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from user.models import UserProfile
from .models import Comment
import readings

def index(request):
    user = request.user
    if user.is_authenticated:
        return render(request, 'br/home.html')
    else:
        return render(request, 'br/index.html')


@login_required
def friend_view(request):
    user = request.user
    profile = user.userprofile
    friends = profile.friends.all()

    print(friends)

    return render(request, 'br/friend_view.html', {'friends': friends, 'friend_count': len(friends)})


@login_required
def settings(request):
    comments = Comment.objects.filter(author=request.user).order_by('-date_posted')
    return render(request, 'br/settings.html', {'comments': comments})


@login_required
def new_friend(request):
    if request.method == 'POST':
        user = request.user
        search = request.POST.get("username")

        user_x = User.objects.filter(username=search).exists()

        if user_x:
            profile = User.objects.get(username=search)
            return redirect('/profile/' + profile.username)

        else:
            messages.error(request, f"No user with the username {search}")

    return render(request, 'br/new_friend.html')


@login_required
def reading(request, number):
    if request.method == 'POST':
        print('POST REQUEST')
        user = request.user
        title = request.POST.get('title')
        text = request.POST.get('text')
        verse = request.POST.get('verse')

        Comment.objects.create(author=user, title=title, text=text, verse=verse)

        return redirect('index')

    try:
        return render(request, 'br/reading.html', {'reading': readings.rng('testplan1', int(number))[2], 'reference': readings.rng('testplan1', int(number))[1], 'copyright': readings.rng('testplan1', int(number))[0]})
    except:
        messages.error(request, "ERROR: Reading plan does not exist :(")
        return redirect('index')


@login_required
def profile(request, username):
    usr = get_object_or_404(User, username=username)
    if request.method == 'POST':
        if usr != request.user:
            request.user.userprofile.friends.add(usr)
            return redirect('index')
            messages.success(request, f'User {usr.username} added to friends!')
        else:
            return redirect('index')
            messages.error(request, "You cannot add yourself. Don't be lonely!")

    else:
        if usr in request.user.userprofile.friends.all():
            at = False
        else:
            at = True
    return render(request, 'br/profile.html', {'usr': usr, 'comments': Comment.objects.filter(author=usr), 'at':at})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        new_username = request.POST.get('field1')
        if len(User.objects.filter(username=new_username)) == 0:
            request.user.username = new_username
            request.user.save()
            messages.success(request, f'username updated to {new_username}')
        else:
            messages.error(request, 'Username with that name already exists')

        return redirect('index')

    return render(request, 'br/profile_edit.html')


@login_required
def password(request):
    if request.method == 'POST':
        cp = request.POST.get('cp')
        new_password = request.POST.get('password')
        password_conf = request.POST.get('password2')
        if cp == request.user.password:
            if new_password == password_conf:
                request.user.password = new_password
                return redirect('index')
                messages.success(request, 'Your password was changed')
            else:
                messages.error(request, 'passwords did not match')
        else:
            messages.error(request, 'Your password was incorrect')

    return render(request, 'br/password.html')
