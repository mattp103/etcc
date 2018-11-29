from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.index, name="index"),
    path('reading/', v.reading, name="reading"),
    path('profile/<username>', v.profile, name="profile"),
    path('settings/', v.settings, name="settings"),
    path('friends/', v.friend_view, name="friends"),
    path('friends/new/', v.new_friend, name="new_friend"),
    # path('comment/new/', v.comment_create, name="new_comment"),
]
