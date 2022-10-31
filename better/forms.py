from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from. models import mod_faq,com_section,com_section_content






class new_user(UserCreationForm):
	first_name=forms.CharField(max_length=300,required=True,widget=forms.TextInput(attrs={'placeholder':'First Name'}))
	surname=forms.CharField(max_length=300,required=True,widget=forms.TextInput(attrs={'placeholder':'surname'}))
	DOB=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'DOB'}))
	phone_number=forms.IntegerField()
	email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Email'}))
	home_address=forms.CharField(max_length=800,widget=forms.TextInput(attrs={'placeholder':'Home_Address'}))
	
	class Meta:
		model=User
		fields=('username','first_name','surname','DOB','phone_number','email','home_address','password1','password2')
			

class user_login_form(forms.Form):
	username=forms.CharField(max_length=300,widget=forms.TextInput(attrs={'placeholder':'username'}))
	password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'password'}))



class faq_form(forms.ModelForm):
	class Meta:
		model=mod_faq
		fields=("name","Question")


class comment_section(forms.ModelForm):
	class Meta:
		model=com_section
		fields=("name","message")


class comment_section_content(forms.ModelForm):
	class Meta:
		model=com_section_content
		fields=("name","message")