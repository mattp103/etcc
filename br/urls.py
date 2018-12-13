from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.index, name="index"),
    path('reading/<plan>/<number>', v.reading, name="reading"),
    # path('home/', v.home, name="home"),
    path('profile/<str:username>', v.profile, name="profile"),
    path('settings/', v.settings, name="settings"),
    path('friends/', v.friend_view, name="friends"),
    path('friends/new/', v.new_friend, name="new_friend"),
    path('settings/edit/username/', v.edit_profile, name="profile-edit"),
    path('settings/edit/password/', v.password, name="password-edit"),
]
