from django import forms
from .models import Articles, Comments
from django import forms

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ('title', 'content', 'image',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('content', )
