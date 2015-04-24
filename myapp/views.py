from django.views import generic

from myapp import forms
from myapp.models import Comment


class IndexView(generic.ListView):
    template_name = 'myapp/index.html'
    model = Comment
    context_object_name = "Comments_list"


class LoginFormView(generic.TemplateView):
    template_name = 'myapp/login.html'


class CommentCreateView(generic.CreateView):
    template_name = 'myapp/create_comment.html'
    form_class = forms.CommentCreateForm
    success_url = "/"


class CommentUpdateView(generic.CreateView):
    template_name = 'myapp/update_comment.html'
    form_class = forms.CommentUpdateForm
    success_url = "/"
