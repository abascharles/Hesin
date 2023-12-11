from django.urls import re_path, path

from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings


urlpatterns = [
    re_path(r'^signup/$', views.signup, name='signup'),
    re_path(r'^login/$', auth_views.LoginView.as_view(template_name="user/login.html"), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(template_name="user/logout.html"), name='logout'),
]
