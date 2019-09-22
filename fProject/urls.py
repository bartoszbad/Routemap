"""fProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from routemap.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name="routes"),
    path('photo_spots/', SpotsView.as_view(), name="spots"),
    path('about_page/', AboutPageView.as_view(), name="about_page"),
    path('about_me/', AboutMeView.as_view(), name="about_me"),
    path('register/', AddUserView.as_view(), name="register"),
    path('login_view/', LoginView.as_view(), name="login_view"),
    path('logout/', LogoutView.as_view()),
    path('add_route/', AddRouteView.as_view(), name="add_route"),
    path('add_photo_spot/', AddSpotView.as_view(), name="add_spot"),
    path('lists/', UserListsView.as_view(), name="lists"),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)