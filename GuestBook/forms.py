from django import forms
from .models import BookGuest


class BookForm(forms.ModelForm):
    class Meta:
        model = BookGuest
        fields = ('name', 'email', 'link', 'textMessage', 'img')
