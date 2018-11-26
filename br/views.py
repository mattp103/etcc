from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'br/index.html')

@login_required
def friend_view(request):
    user = request.user
    friends = user.userprofile.friends

    print(friends)

    return render(request, 'br/friend_view.html', {'friends': friends})
