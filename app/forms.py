from app.models import *
from django import forms 
class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username','password','email']
        widgets={'password':forms.PasswordInput}
class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        exclude=['username']

