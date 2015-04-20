from django.conf.urls import patterns, url
from myapp import views


urlpatterns = patterns(
    '',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^login/$', views.LoginFormView.as_view(), name='login'),
    url(r'^create-comment/$', views.CommentCreateView.as_view(
        success_url="/myapp/"),
        name='create'),
    # url(r'^login/$', auth_views.login),

    # url(r'^logout/$', views.LogoutRedirectView.as_view(), name='logout'),

)
