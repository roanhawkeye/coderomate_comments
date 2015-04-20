from django.conf.urls import patterns, url
from myapp import views
from django.contrib.auth import views as auth_views


urlpatterns = patterns(
    '',
    url(r'^$', views.indexView.as_view(), name='index'),
    url(r'^login/$', views.LoginFormView.as_view(), name='login'),
    # url(r'^login/$', auth_views.login),

    # url(r'^logout/$', views.LogoutRedirectView.as_view(), name='logout'),

)
