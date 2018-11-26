from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.index, name="index"),
    path('friends/', v.friend_view, name="friend")
]
