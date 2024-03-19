"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mysite import views
from challenges import views as cviews
from settings import views as sviews
from login import views as lviews
from home import views as hviews
from .views import gallery_view, like_image
from userProtection import views as upviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hviews.home, name='home'),
    path('base/', views.base, name='base'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path("challenges/", cviews.render_map, name="challenges"),

    path("settings/", sviews.render_settings, name="settings"),
    path("settings/delete_account/", sviews.delete_account, name="delete_account"),
    path("settings/changePassword/", sviews.changePassword, name="changePassword"),
    path("settings/changeUsername/", sviews.changeUsername, name="changeUsername"),
    path("settings/logoutUser/", sviews.logoutUser, name="logoutUser"),

    path('login/', lviews.logins, name='login'),
    path('register/', lviews.register, name='register'),
    path('userProtection/', upviews.render_userProtection, name='userProtection'),

    path('gallery/',gallery_view, name='gallery'),
    path('like-image/',like_image,name='like-image')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)