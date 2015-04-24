from django.conf.urls import patterns, url
from myapp import views


urlpatterns = patterns(
    '',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^login/$', views.LoginFormView.as_view(), name='login'),
    url(r'^create-comment/$', views.CommentCreateView.as_view(),
        name='create'),
    url(r'^update-comment/$', views.CommentUpdateView.as_view(),
        name='update'),

)
