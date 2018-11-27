from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.index, name="index"),
    path('reading/', v.reading, name="reading"),
    path('settings/', v.settings, name="settings"),
    path('friends/', v.friend_view, name="friends"),
    # path('friends/new/', v.new_friend, name, name="remove_friends"),
    # path('comment/new/', v.comment_create, name="new_comment"),
]
