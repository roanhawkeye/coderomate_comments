from django import forms

from myapp.models import Comment


class CommentCreateForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = [
            'body', 'is_inappropriate', 'ranking'
        ]
