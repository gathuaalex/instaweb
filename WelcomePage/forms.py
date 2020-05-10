from django import forms 
from django.contrib.auth.models import User 
from WelcomePage.models import UserProfiles

#inherits from class forms
class UserForm(forms.ModelForm): 
    #passwordinput() widget is used for hidding the password
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta: 
        model = User #its must to supply the model field
        fields = ('username', 'email', 'password')#this shows the fields that should be present in the rendered form
class UserProfileForm(forms.ModelForm): 
     class Meta: 
         model = UserProfiles
         fields = ('website', 'picture' ,'contact','firstname','lastname')
