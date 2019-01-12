from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.index, name="index"),
    path('reading/<number>', v.reading),
    # path('home/', v.home, name="home"),
    path('profile/<str:username>', v.profile),
    path('settings/', v.settings, name="settings"),
    path('friends/', v.friend_view, name="friends"),
    path('friends/new/', v.new_friend, name="new_friend"),
    path('settings/edit/username/', v.edit_profile, name="profile-edit"),
    path('settings/edit/password/', v.password, name="password-edit"),
    path('settings/edit/comment/<int:c_pk>', v.comment_edit),
    path('settings/delete/comment/<int:c_pk>', v.comment_delete),
    path('groups/', v.groups, name="groups"),
    path('groups/<code>/', v.group),
]
