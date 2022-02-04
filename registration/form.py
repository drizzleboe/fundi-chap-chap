from django import forms
from .models import users
import datetime

#create your form here
class sign_in(forms.Form):
    username=forms.CharField(label="username")
    passwd  =forms.CharField(label="password")
    
class signups(forms.Form):
    fname=forms.CharField(label='first name', help_text='')
    lname=forms.CharField(label='last name')
    phone =forms.CharField(label='0700 000 000')
   # date_of_birth=forms.DateField(initial=datetime.date.today)

class location(forms.ModelForm):    
    class Meta:
        model=users
        fields=['location']

class service(forms.ModelForm):    
    class Meta:
        model=users
        fields=['profession']

class image(forms.ModelForm):    
    class Meta:
        model=users
        fields=['image']