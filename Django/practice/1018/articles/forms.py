from django import forms
from .models import Articles, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', ]