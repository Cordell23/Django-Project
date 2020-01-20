from django import forms
from .models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ObjectDoesNotExist
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User



class RegisterForm(forms.ModelForm):

	first_name 	= forms.CharField(required= True, max_length= 50)
	last_name 	= forms.CharField(required= True, max_length= 50)
	email 		= forms.EmailField(required= True, max_length= 80)
	username 	= forms.CharField(required= True, max_length= 100)
	password 	= forms.CharField(label= 'Password', required= True, max_length= 100, widget= forms.PasswordInput)
	password1	= forms.CharField(label= 'Password Confirmation', required= True, max_length= 100, widget= forms.PasswordInput)


	class Meta:
		model 	= User
		fields 	= {
			"first_name",
			"last_name",
			"username",
			"email",
			"password"
		}

	def clean_password(self):
		# Check to see if the password entries match
		password 	= self.cleaned_data.get("password")
		password1	= self.cleaned_data.get("password1")
		if password != password1:
			raise forms.ValidationError("Passwords do not match!")
		return password





class LoginForm(forms.Form):

	# email 			= forms.EmailField(required= True,max_length= 80)
	username		= forms.CharField(required= True, max_length= 80)
	password 		= forms.CharField(required= True, max_length= 100,  widget=forms.PasswordInput)


	# def clean_email(email):
	# 	"""
	# 	Validate email against the database
	# 	"""

	# 	try:
	# 		User.objects.get(user__email= email)
	# 	except ObjectDoesNotExist:
	# 		raise forms.ValidationError("User does not exist!")
	# 	return user__email
	# 	user = authenticate(username=username, password=password)

	def clean_username(username):
		try:
			# User.objects.get(username= username)
			user = authenticate(username= username)
			print('in the user form')
		except ObjectDoesNotExist:
			print('issue is with username')
			raise forms.ValidationError("User does not exist!")
		return user



	def clean_password(password):
		"""
		To validate you should use the django check_password
		"""
		# user = User.objects.last()
		try:
			# user_password = self.cleaned_data['password']
			check_password(password, User.password)
			print('password checked')
		except:
			print('password exception hit')
			raise forms.ValidationError('Password is incorrect')
		return password


	def get_user(self):
		self.authed_user = authenticate(user, password)
		print('user password')
		return self.authed_user