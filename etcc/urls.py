from django.contrib import admin
from django.urls import path, include
from user import views as uv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('br.urls')),
    path('login/', uv.signin, name="login"),
    path('register/', uv.signup, name="register"),
    path('logout/', uv.signout, name="logout"),
    path('auth/', include('social_django.urls', namespace='social')),
]
