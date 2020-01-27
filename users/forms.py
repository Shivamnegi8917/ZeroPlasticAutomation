from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PlasticData

class SignUpForm(UserCreationForm):
	email = forms.EmailField(
		label='',
		max_length=254,
		widget=forms.EmailInput(
			attrs={
				"placeholder": "Email",
				"class": "form-control"
			}
		)
	)

	username = forms.CharField(
		label='',
		max_length=30,
		min_length=5,
		required=True,
		widget=forms.TextInput(
			attrs={
				"placeholder": "Username",
				"class": "form-control"
			}
		)
	)

	password1 = forms.CharField(
		label='',
		max_length=30,
		min_length=8,
		required=True,
		widget=forms.PasswordInput(
			attrs={
				"placeholder": "Password",
				"class": "form-control"
			}
		)
	)

	password2 = forms.CharField(
		label='',
		max_length=30,
		min_length=8,
		required=True,
		widget=forms.PasswordInput(
			attrs={
				"placeholder": "Confirm Password",
				"class": "form-control"
			}
		)
	)
	
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')


class ShopDetailsForm(forms.Form):
	shopname = forms.CharField(
		label='',
		max_length=254,
		widget=forms.TextInput(
			attrs={
				"placeholder": "shop name",
				"class": "form-control"
			}
		)
	)

	product = forms.CharField(
		label='',
		max_length=200,
		required=True,
		widget=forms.TextInput(
			attrs={
				"placeholder": "Product",
				"class": "form-control"
			}
		)
	)

	quantity = forms.IntegerField(
		required=True,
		widget=forms.NumberInput(
			attrs={
				"placeholder": "quantity"
			}
		)
	)
	types_of_plastics = []
	plastic_type = forms.ChoiceField(
		required=True,
		widget=forms.RadioSelect(
			choices=types_of_plastics,
			attrs={
				"class": "form-control"
			}
		)
	)

	status_of_plastic = ['recycled','bought','used','declined']
	status = forms.ChoiceField(
		required=True,
		widget=forms.RadioSelect(
			choices=status_of_plastic,
			attrs={
				"class": "form-control"
			}
		)
	)
	
	class Meta:
		model = PlasticData
		fields = ('shopname','product','quantity','plastic_type','status')
