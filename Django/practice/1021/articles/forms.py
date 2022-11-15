from django import forms
from django import forms
from .models import Review, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title','content','movie_name','grade','genre','image',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)