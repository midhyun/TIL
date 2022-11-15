from django import forms
from django import forms
from .models import Articles, Comments

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ('title', 'content', 'image',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('content',)