from django.views import generic

from myapp import forms
from myapp.models import Comment


class IndexView(generic.ListView):
    template_name = 'myapp/index.html'
    model = Comment


class LoginFormView(generic.TemplateView):
    template_name = 'myapp/login.html'


class CommentCreateView(generic.CreateView):
    template_name = 'myapp/create_comment.html'
    form_class = forms.CommentCreateForm
