from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Post, Tag


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'body', 'image', 'date_pub', 'tags')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': '10'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'date_pub': forms.DateTimeInput(format='%Y-%m-%dT%H:%M', attrs={'class': 'form-control vDateField', 'type': 'datetime-local'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Название статьи',
            'slug': 'Человеко-понятный уникальный идентификатор',
            'body': 'Текст статьи',
            'image': 'Изображение',
            'date_pub': 'Время публикации',
            'tags': 'Теги'
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('title', 'slug')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            'title': 'Наименование тега',
            'slug': 'Человеко-понятный уникальный идентификатор'
        }


class AuthUserForm(AuthenticationForm, forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control mb-3'
