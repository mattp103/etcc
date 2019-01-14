from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

def username(request):
    if request.method == 'POST':
        search = request.GET.get("username")
        if User.objects.filter(username=search).exists():
            return HttpResponse("true")
        else:
            return HttpResponse("false")
