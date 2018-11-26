from django.shortcuts import render
from user.models import Friend
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'br/index.html')

@login_required
def friend_view(request):
    user = request.user
    friends = Friend.objects.filter(current_user=user).users

    for user_ob in friends:
        print(user_ob.username)

    return render(request, 'br/friend_view.html', {'friends': friends})
