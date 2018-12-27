from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Answer
from django.views.generic import ListView

from django.urls import reverse 
from django.contrib.auth import authenticate, login, logout
from questions.forms import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect
# Create your views here.

def questionsPage(request):
	#questions_list = Question.objects.all() - without answers count
	questions_list = Question.objects.newest()
	context_object_name = 'questions'
	questions, page = paginating(questions_list, request)
	user_profile = Profile.objects.getProfile(request.user)
	return render(request, 'questionList.html', {
		"questions": questions,
		"page": page, 
		"sort": "new", 
		'page_alias': 'questionList',
		'user_profile': user_profile,
		})

def hot(request):
	questions_list = Question.objects.hottest()
	context_object_name = 'questions'
	questions, page = paginating(questions_list, request)
	user_profile = Profile.objects.getProfile(request.user)
	return render(request, 'hot.html', {
		"questions": questions,
		"page": page, 
		"sort": "new", 
		'page_alias': 'hot',
		'user_profile': user_profile,
		})


def all_tags_view(request):
	user_profile = Profile.objects.getProfile(request.user)
	tags_list = Tag.objects.all()
	#allTags, page = paginating(tags_list, request)
	return render(request, 'allTags.html', {
		'tags': tags_list,
		'page_alias': 'allTags',
		'user_profile': user_profile,
		})


def tag(request, tag_name):
	questions_list = Question.objects.byTag(tag_name)
	questions, page = paginating(questions_list, request)
	user_profile = Profile.objects.getProfile(request.user)
	return render(request, 'tagQuestion.html', {
		'questions': questions,
		'page_alias': 'tag',
		'tag_name': tag_name, #to show in tag page
		'user_profile': user_profile,
		})
    #res = render ...
    #return HttpResponse(res)
def question(request, question_id):
	question = Question.objects.withId(question_id)
	answers = Answer.objects.hottest(question_id)
	user_profile = Profile.objects.getProfile(request.user)
	page = paginating(answers, request)

	#if request.user.is_authenticated():
	if request.user.id != None:
		if request.method == "POST":
			form = AnswerForm(request.POST) #binding data to the form
			if form.is_valid():
				answer = form.save(commit=False)
				answer.author = request.user.profile
				answer.question = question
				answer.save()
				#page_number = answer.get_page()
				return redirect('/question/' + str(question_id), pk=answer.pk)
		else:
			form = AnswerForm()
	else:
		form = 'empty'

	context = {
	'question': question, 
	'answers': answers, 
	'page': page, 
	'form': form,
	'user_profile': user_profile,
	}
	return render(request, "question.html", context)

@login_required(login_url='signin')
def ask(request):
	user_profile = Profile.objects.getProfile(request.user)
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
		#'form': form ,
		'page_alias': 'ask',
		'user_profile': user_profile,
		})

@csrf_protect
def signIn(request):
	form = SignInForm(data=request.POST or None)
	if request.POST and form.is_valid():		
		user = form.login(request) #get user
		if user:
			login(request, user) #login user
			if 'next' in request.POST: #getting next from url in login.html
				return redirect(request.POST.get('next'))
			else:
				return redirect('base_questions')

	return render(request, 'login.html', {
		'form': form,
		'page_alias': 'signIn'
		})


"""def another way to sign in (request):
	if request.POST:
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			#login the user
			user = form.get_user()
			login(request, user)
			return redirect('base_questions')
	else:
		form = AuthenticationForm()
	return render(request, 'login.html', {
		'form': form,
		})"""

def logout_view(request):
	logout(request)
	#return redirect(reverse('index'))
	return redirect('base_questions')

def signUp(request):
	return render(request, 'signup.html', {
		'header': 'some text',
		'page_alias': 'signUp'
		})

def settings(request, user_name):
	user_profile = Profile.objects.getProfile(request.user)
	return render(request, 'mysettings.html', {
		'page_alias': 'settings',
		'user_profile': user_profile,
		})
    #res = render(request, 'mysettings.html')
    #return HttpResponse(res)

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
def loggggin(request):
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