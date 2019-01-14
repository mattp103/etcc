from django.urls import path
from . import views as v

urlpatterns = [
    path('api/username', v.username, name="username"),
]
