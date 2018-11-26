from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.index, name="index"),
    path('friends/', v.friend_view, name="friends"),
    # path('friends/new/', v.new_friend_view, name="new_friends"),
    # path('friends/remove/', v.remove_friend_view, name="remove_friends"),
    path('comment/new/', v.comment_create, name="new_comment"),
]
