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

    plan = 'testplan1'
    try:
        return render(request, 'br/reading.html', {'reading': readings.rng(plan, int(number))[2], 'reference': readings.rng(plan, int(number))[1], 'v': readings.rng(plan, int(number))[1].split(":")[0], 'copyright': readings.rng(plan, int(number))[0], 'next': int(number) + 1})
    except:
        messages.error(request, "ERROR: Reading plan does not exist :(")
        return redirect('index')


@login_required
def comment_edit(request, c_pk):
    comment = get_object_or_404(Comment, pk=c_pk)

    if request.method == 'POST':
        if comment.author == request.user:
            comment.title = request.POST.get('title')
            comment.verse = request.POST.get('verse')
            comment.text = request.POST.get('text')
            comment.save()

            messages.success(request, 'Comment Updated')
            return redirect('settings')


    return render(request, 'br/comment_edit.html', {'comment': comment})


@login_required
def comment_delete(request, c_pk):
    comment = get_object_or_404(Comment, pk=c_pk)

    if request.method == 'POST':
        if comment.author == request.user:
            comment.delete()
            messages.success(request, 'Comment Deleted')
            return redirect('settings')

    return render(request, 'br/comment_delete.html', {'comment': comment})


@login_required
def profile(request, username):
    usr = get_object_or_404(User, username=username)
    if request.method == 'POST':
        if usr != request.user:
            request.user.userprofile.friends.add(usr)
            messages.success(request, f'User {usr.username} added to friends!')
            return redirect('index')
        else:
            messages.error(request, "You cannot add yourself. Don't be lonely!")
            return redirect('index')

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
            return redirect('index')
        else:
            messages.error(request, 'Username with that name already exists')


    return render(request, 'br/profile_edit.html')


@login_required
def password(request):
    if request.method == 'POST':
        cp = request.POST.get('cp')
        new_password = request.POST.get('password')
        password_conf = request.POST.get('password2')
        if request.user.check_password(cp):
            if new_password == password_conf:
                request.user.set_password(new_password)
                request.user.save()
                messages.success(request, 'Your password was changed')
                return redirect('login')
            else:
                messages.error(request, 'passwords did not match')
        else:
            messages.error(request, 'Your password was incorrect')

    return render(request, 'br/password.html')
