from django.views import generic
# from django.contrib.auth.decorators import login_required


# @login_required
class indexView(generic.TemplateView):
    template_name = 'myapp/index.html'


class LoginFormView(generic.TemplateView):
    template_name = 'myapp/login.html'
