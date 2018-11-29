from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from user.models import UserProfile
from .models import Comment


def index(request):
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
def reading(request):
    if request.method == 'POST':
        print('POST REQUEST')
        user = request.user
        title = request.POST.get('title')
        text = request.POST.get('text')
        verse = request.POST.get('verse')

        Comment.objects.create(author=user, title=title, text=text, verse=verse)

        return redirect('index')

    return render(request, 'br/reading.html')


def profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'br/profile.html', {'user': user, 'comments': Comment.objects.filter(author=user)})


def edit_profile(request):
    pass
