from django.urls import re_path, path
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    re_path(r'^$', views.header, name="header"),
    re_path(r'^self/$', views.about, name="about"),
    re_path(r'^get_verified/$', views.club, name="club"),
    re_path(r'^not_verified/$', views.not_verified, name="not_verified"),
    re_path(r'^admin_verify/$', views.verify_from_admin, name="verification_from_admin"),
    re_path(r'^verified_as_true/(?P<pk>\d+)/$',views.Verification_Status_True, name="verified_as_true"),
    re_path(r'^verified_as_false/(?P<pk>\d+)/$',views.Verification_Status_False, name="verified_as_false"),
    re_path(r'^mail_Y/$', views.mail_Y, name="mail_of_acceptance"),
    re_path(r'^mail_N/$', views.mail_N, name="mail_of_rejectance"),
    re_path(r'^post_request/$', views.post_request, name="post_request"),
    re_path(r'^fund_request/$', views.donation,name="fund request"),
    re_path(r'^payment/$', views.payment, name='payment'),
    re_path(r'^charge/$', views.charge, name="charge"),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)