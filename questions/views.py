from django.shortcuts import render
from django.http import HttpResponse

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

def tag(request, tag_name):
    res = render(request, 'tagQuestion.html')
    return HttpResponse(res)


def question(request, question_id):
    response = "You're looking at the results of question %s."
    res = render(request, 'question.html')
    return HttpResponse(res)

def results(request, question_id):
		number = request.GET.get('id',' ')


def settings(request, user_name):
    res = render(request, 'mysettings.html')
    return HttpResponse(res)

def paginate(objects_list, request):
    # do smth with Paginator, etc…
    return objects_page, paginator