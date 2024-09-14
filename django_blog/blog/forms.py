
from os import name
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
# blog/forms.py
from blog.models import Post , Tag

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']


# forms.py
from django import forms
from django.utils.safestring import mark_safe
from .models import Tag, Post

class TagWidget(forms.TextInput):
    def render(self, name, value, attrs=None, renderer=None):
        # Custom rendering logic for the widget, e.g., with autocompletion
        return mark_safe(f'<input type="text" name="{name}" value="{value}" class="custom-tag-widget">')

class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=TagWidget(attrs={'class': 'tag-input', 'placeholder': 'Add tags'}),
        required=False
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
