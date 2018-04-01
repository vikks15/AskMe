from django.shortcuts import render

# Create your views here.

def base(request):
	return render(request, 'base.html', {
		'questions': [ ],
		'header': 'New Questions',
		})

def hot(request):
	return render(request, 'index.html', {
		'questions': [ ],
		'header': 'some text'
		})

def ask(request):
	return render(request, 'ask.html', {
		'header': 'some text'
		})

def signIn(request):
	return render(request, 'login.html', {
		'header': 'some text'
		})

def signUp(request):
	return render(request, 'signup.html', {
		'header': 'some text'
		})

def tag(request):
	return render(request, 'tagQuestion.html', {
		'header': 'some text'
		})

def question(request):
	return render(request, 'question.html', {
		'header': 'some text'
		})

def settings(request):
	return render(request, 'mysettings.html', {
		'header': 'some text'
		})

def menu_switch(url):
	if url == 'base_questions':
		return true
	else:
		return false