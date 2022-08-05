from .models import costomer
from django.forms import ModelForm
from django.forms import ModelForm, TextInput

class costomerForm(ModelForm):
	class Meta:
		model = costomer
		fields = ['name', 'surename', 'username']

		widgets = {
			"name": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'First name'
				}),
			"surename": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Surename'
				}),
			"username": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'mail'
				}),
		}