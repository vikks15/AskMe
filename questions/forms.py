from django import forms

class AskForm(forms.Form):
	title = forms.CharField(
		widget=forms.TextInput (
			attrs = {'class': 'form-control' }
			)
		)
	text = forms.CharField(
		widget=forms.Textarea (
			attrs = {'class': 'form-control' }
			)
		)
	tags = forms.CharField(
		widget=forms.Textarea (
			attrs = {'class': 'form-control' }
			)
		)
	pass


class AnswerForm (forms.Form):
	text = forms.CharField(
		widget=forms.Textarea (
			attrs = {'class': 'form-control' }
			)
		)
	pass

class LoginForm(forms.Form):
	loginField = forms.CharField(
		widget=forms.TextInput (
			attrs = {'class': 'form-control' }
			)
		)
	passField = forms.CharField(
		widget=forms.TextInput (
			attrs = {'class': 'form-control' }
			)
		)
	pass

class RegisterForm(forms.Form):
	login = forms.CharField(
		widget=forms.TextInput (
			attrs = {'class': 'form-control' }
			)
		)
	email = forms.CharField(
		widget=forms.TextInput (
			attrs = {'class': 'form-control' }
			)
		)
	nickname = forms.CharField(
		widget=forms.TextInput (
			attrs = {'class': 'form-control' }
			)
		)
	password = forms.CharField(
		widget=forms.TextInput (
			attrs = {'class': 'form-control' }
			)
		)
	repeatpass = forms.CharField(
		widget=forms.TextInput (
			attrs = {'class': 'form-control' }
			)
		)
	#avatar

	pass

class SettingsForm(forms.Form):
	email = forms.CharField(
		widget=forms.TextInput (
			attrs = {'class': 'form-control' }
			)
		)
	nickname = forms.CharField(
		widget=forms.TextInput (
			attrs = {'class': 'form-control' }
			)
		)
	password = forms.CharField(
		widget=forms.TextInput (
			attrs = {'class': 'form-control' }
			)
		)
	repeatpass = forms.CharField(
		widget=forms.TextInput (
			attrs = {'class': 'form-control' }
			)
		)
	#avatar
	pass
