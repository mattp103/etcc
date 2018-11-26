from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from user.models import UserProfile

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
def comment_create(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST.get('title')
        text = request.POST.get('text')
        verse = request.post.get('verse')

        Comment.objects.create(author=user, title=title, text=text, verse=verse)
