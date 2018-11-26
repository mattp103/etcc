from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from user.models import UserProfile
from .models import Comment

def index(request):
    return render(request, 'br/index.html')

def reading(request):
    return render(request, 'br/reading.html')

@login_required
def friend_view(request):
    user = request.user
    profile = user.userprofile
    friends = profile.friends.all()

    print(friends)

    return render(request, 'br/friend_view.html', {'friends': friends, 'friend_count': len(friends)})

# def new_friend(request):
#     if request.method == 'POST':
#         pass
#
#     pass

@login_required
def comment_create(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST.get('title')
        text = request.POST.get('text')
        verse = request.post.get('verse')

        Comment.objects.create(author=user, title=title, text=text, verse=verse)

        return redirect('index')

    return render(request, 'br/reading.html')
