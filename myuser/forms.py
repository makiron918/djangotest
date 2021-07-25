from django import forms

from .models import MyUser

class PostForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ('username', 'age', 'email')