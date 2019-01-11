from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from user.models import UserProfile
from .models import *
import readings
from time import strftime

def index(request):
    user = request.user
    if user.is_authenticated:
        d = int(strftime("%j"))-1
        # checks for progress objects
        for reading in Reading.objects.filter(date=d):
            if len(Progress.objects.filter(usr=user, reading=reading)) == 0:
                Progress.objects.create(reading=reading, usr=user, status=False)

        t_progs = []

        for reading in Reading.objects.filter(date=d):
            po = Progress.objects.get(usr=request.user, reading=reading)
            t_progs.append(po.status)

        z = zip(t_progs, readings.readings_today("testplan1"))

        return render(request, 'br/home.html', {'readings': readings.readings_today("testplan1"), 't_p': t_progs, 'zp': z})
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
    if request.method == 'POST':
        new_bible_ver = request.POST.get("bible_ver")
        if new_bible_ver in readings.versions:
            u = request.user.userprofile
            u.bible_ver = new_bible_ver
            b = request.POST.get('bio')
            d = request.POST.get('description')
            u.desc = d
            u.bio = b
            messages.success(request, "Settings updated")
            u.save()
            print(u.bio)

            return redirect('settings')
        else:
            messages.error(request, f"No bible version with the name {new_bible_ver}")
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
    reading_data = readings.rng("testplan1", int(number), request.user.userprofile.bible_ver)
    if 'armel' in request.POST:
        print('POST REQUEST')
        user = request.user
        title = request.POST.get('title')
        text = request.POST.get('text')
        if request.POST.get('verse') > reading_data[1].split("-")[-1]:
            messages.error(request, "Invalid Verse")
            return redirect('/')
        verse = reading_data[1].split(":")[0] + ":" + request.POST.get('verse')

        Comment.objects.create(author=user, title=title, text=text, verse=verse, reading=Reading.objects.get(date=int(strftime("%j"))-1, r=readings.jr("testplan1", int(number))))

        return redirect('/reading/'+number)

    elif 'glen' in request.POST:
        print("yep")
        r = Progress.objects.get(usr=request.user, reading=Reading.objects.get(date=int(strftime("%j"))-1, r=readings.jr("testplan1", int(number))))
        print("got progress object")
        r.status = True
        print("updated status")
        print(r.status)
        r.save()
        print("saved p object")
        print(r.status)

        n = request.POST.get('redirect')
        print(n)

        return redirect('/reading/' + n)

    t_progs = []
    d = int(strftime("%j"))-1
    for reading in Reading.objects.filter(date=d):
        po = Progress.objects.get(usr=request.user, reading=reading)
        t_progs.append(po.status)

    return render(request, 'br/reading.html',
    {'reading': reading_data[2], 'reference': reading_data[1],
     'v': reading_data[1].split(":")[0], 'lv': reading_data[1].split("-")[-1],
      'copyright': reading_data[0], 'current_num': int(number),
      'notes': Comment.objects.filter(reading=Reading.objects.get(date=int(strftime("%j"))-1, r=readings.jr("testplan1", int(number)))),
      't_p': t_progs[int(number)]})


    # 'notes': Comment.objects.filter(author=request.user.userprofile.friends.all()[0],
    # reading=Reading.objects.get(r=readings.jr(int(number))))})
    # except:
    #     messages.error(request, "ERROR: Reading plan does not exist :(")
    #     return redirect('index')


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
            messages.error(request, "You can't add yourself. Don't be lonely!")
            return redirect('index')
    else:
        if usr in request.user.userprofile.friends.all():
            at = False
        else:
            at = True
        if usr == request.user:
            cp = True
        else:
            cp = False
    return render(request, 'br/profile.html', {'usr': usr, 'comments': Comment.objects.filter(author=usr).order_by('-date_posted'), 'at': at, 'cp': cp})


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

@login_required
def groups(request):
    if request.method == 'POST':
        user = request.user
        search = request.POST.get("code")

        group_x = readingGroup.objects.filter(code=search).exists()

        if group_x:
            group = readingGroup.objects.get(code=search)
            return redirect('/groups/' + group.code)

        else:
            messages.error(request, f"No group with the code {search}")

    return render(request, 'br/groups.html')

@login_required
def group(request, code):
    gp = get_object_or_404(readingGroup, code=code)
    # if request.method == 'POST':
    #     if usr != request.user:
    #         request.user.userprofile.friends.add(usr)
    #         messages.success(request, f'User {usr.username} added to friends!')
    #         return redirect('index')
    #     else:
    #         messages.error(request, "You can't add yourself. Don't be lonely!")
    #         return redirect('index')
    # else:
    if request.user in gp.members.all():
        in_group = False
    else:
        in_group = True
    if request.user == gp.admin:
        admin = True
    else:
        admin = False
    return render(request, 'br/group_veiw.html', {'gp': gp, 'in_group': in_group, 'admin': admin})
