from dataclasses import field
from django import forms
from .models import *

class Student_form(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class Personal_details_form(forms.ModelForm):
    class Meta:
        model = Personal_details
        fields = '__all__'

class Payment_details_form(forms.ModelForm):
    class Meta:
        model = Payment_details
        fields = '__all__'

class Course_details_form(forms.ModelForm):
    class Meta:
        model = Course_details
        fields = '__all__'

class Myform(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
        'class':'form-control',
        'placeholder':'Username'

        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
        'class':'form-control',
        'placeholder':'Password'
        }
    ))

class Studentimgform(forms.ModelForm):
    class Meta:
        model = Student_img
        fields = '__all__'