from django import forms

class RoleForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput)
	description = forms.CharField(widget=forms.TextInput)

class DetailForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput)

class Contact(forms.Form):
	pass
