from django import forms
from django.contrib.auth import get_user_model
from .models import Profile
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username =  forms.CharField()
    password =  forms.CharField(widget = forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password  = forms.CharField(label = "password", widget = forms.PasswordInput)
    password2 = forms.CharField(label = "Repeat password", widget = forms.PasswordInput)


    class Meta:
        model  = get_user_model()
        fields = ['username','first_name','email']


    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords do NOT match")

        return cd['password2']

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists(): # Checking if the same email already present in the database
            raise forms.ValidationError("Email already exists. Please use a different email")
        return data


class UserEditForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', "email"]

    #User should not be able to edit the email address to an existing email address in the database.

    def clean_email(self):
        data = self.cleaned_data['email']
        qs   = User.objects.exclude(id = self.instance.id).filter(email = data) #Ensuring the current email is excluded from the query and then search the exisiting emails
        if qs.exists():
            raise forms.ValidationError("Another account exists with same email. Please try a different email")

        return data




class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth', "photo"]




















