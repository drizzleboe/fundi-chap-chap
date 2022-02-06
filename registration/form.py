from django import forms
from .models import user
import datetime

#create your form here
class sign_in(forms.Form):
    username=forms.CharField(label="username")
    passwd  =forms.CharField(label="password")
    
class location(forms.ModelForm):    
    class Meta:
        model=user
        fields=['location']

class prfssn(forms.ModelForm):    
    class Meta:
        model=user
        fields=['prfssn']

class image(forms.ModelForm):    
    class Meta:
        model=user
        fields=['image']