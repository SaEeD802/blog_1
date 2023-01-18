from django import forms
from blog.models import Post


class NewPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'status', 'about', 'author']


class SearchForm(forms.Form):
    search = forms.CharField(max_length=30)