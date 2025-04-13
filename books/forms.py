from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import ProfilePicture


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this email already exists.")
        return email

    def save(self, commit=True):

        user = super().save(commit=False)  
        
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()  
        
        return user

class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = ProfilePicture
        fields = {'name', 'image'}
