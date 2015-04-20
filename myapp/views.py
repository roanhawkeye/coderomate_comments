from django.views import generic

from myapp import forms


class IndexView(generic.TemplateView):
    template_name = 'myapp/index.html'


class LoginFormView(generic.TemplateView):
    template_name = 'myapp/login.html'


class CommentCreateView(generic.CreateView):
    template_name = 'myapp/create_comment.html'
    form_class = forms.CommentCreateForm
