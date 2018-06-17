from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.views.generic import ListView

from django.urls import reverse 
from django.contrib.auth import authenticate, login
from questions.forms import AskForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_protect
# Create your views here.

def questionsPage(request):
	#questions_list = Question.objects.all() - without answers count
	questions_list = Question.objects.newest()
	context_object_name = 'questions'
	questions, page = paginating(questions_list, request)
	return render(request, 'questionList.html', {
		"questions": questions,
		"page": page, 
		"sort": "new", 
		'page_alias': 'questionList'
		})

def hot(request):
	"""return render(request, 'hot.html', {
		'questions': [ ],
		'header': 'some text',
		'page_alias': 'hot'
	})"""
	questions_list = Question.objects.hottest()
	#questions_list = Question.objects.annotate(number_of_answers = Count('answer'))
	context_object_name = 'questions'
	questions, page = paginating(questions_list, request)
	return render(request, 'hot.html', {
		"questions": questions,
		"page": page, 
		"sort": "new", 
		'page_alias': 'hot'
		})

def ask(request):
#	form = AskForm(request.POST or None)
#	if request.POST:
#		if form is_valid():
#			question = Question.objects.create (
#				title = form.cleaned_data.get('title'),
#				text = form.cleaned_data.get('text'),
#				author = request.user,
#				)
#			return redirect (
#				reverse(
#					'question', kwargs={'qid':question.pk} 
#					) 
#				)
	return render(request, 'ask.html', {
		'header': 'some text' ,
		'form': form ,
		'page_alias': 'ask'
		})

def signIn(request):
	if request.POST:
		user = auth.authenticate (
			username = request.POST.get('username'),
			password = request.POST.get('password'),
			)

		if user is not None:
			auth.login(request, user)
			return redirect('/')
	return render(request, 'login.html', {
		'header': 'some text',
		'page_alias': 'signIn'
	})

def logout(request):
	return redirect(reverse('index'))

def signUp(request):
	return render(request, 'signup.html', {
		'header': 'some text',
		'page_alias': 'signUp'
		})

def tag(request, tag_name):
    res = render(request, 'tagQuestion.html', {
    	'page_alias': 'tag'
    	})
    return HttpResponse(res)


def question(request, question_id):
    questions = []
    for i in range(0,30):
    	questions.append({
    	'title': 'title' + str(i),
    	'question_id': i,
    	'text': 'text' + str(i)
    	})
    q = questions[question_id]['title'];
    response = "You're looking at the results of question %s."
    res = render(request, 'question.html', questions[question_id])
    return HttpResponse(res)

def settings(request, user_name):
    #res = render(request, 'mysettings.html')
    #return HttpResponse(res)
    return render(request, 'mysettings.html', {
		'header': 'some text',
		'page_alias': 'settings'
		})

def paginate(objects_list, request):

    # do smth with Paginator, etc…
    return objects_page, paginator


def paginating(object_list, request):
	paginator = Paginator(object_list, 5)
	page = request.GET.get('page')
	try:
		objects = paginator.page(page)
	except PageNotAnInteger:
		objects = paginator.page(1)
	except EmptyPage:
		objects = paginator.page(paginator.num_pages)
	return objects, page;


@csrf_protect
def login(request):
	args = {}
	if request.POST:
		username = request.POST.get('inputLogin', '')
		password = request.POST.get('inputPassword', '')
		user = auth.authenticate(username = username, password = password)
	if user is not None:
		auth.login(request, user)
		return redirect('/')
	else:
		args['login_error'] = "Sorry, you have some error!"
		return render(request, 'login.html', args);