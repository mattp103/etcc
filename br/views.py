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

# @login_required
# def new_friend(request):
#     if request.method == 'POST':
#         user = request.user
#         search = request.POST.get("username")
#
#         user_x = User.objects.filter(username=search).exists()
#
#         if user_x:
#             no_users = False
#             friend_user = User.objects.get(username=search)
#             friend = user.userprofile.friends.add(friend_user)
#
#             messages.success(request, f"User {friend.username} added to friends :)")
#
#         else:
#             no_users = True
#
#     else:
#         no_users = True
#
#     return render(request, 'br/new_friend.html', {'no_users': no_users})


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
