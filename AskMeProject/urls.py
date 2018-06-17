"""AskMeProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from questions import views

urlpatterns = [
	path('admin/', admin.site.urls),
    path('', views.questionsPage, name='base_questions'),
    path('hot/', views.hot, name='hot_questions'),
    path('tag/<slug:tag_name>/', views.tag, name='tag_questions'),
    path('ask/', views.ask, name='ask_question'),
    path('signup/', views.signUp, name='signup'),
    path('settings/<slug:user_name>/', views.settings, name='settings'),
    path('signin/', views.signIn, name='signin'),
    path('question/<int:question_id>/', views.question, name='question_page'),

    
    #path('questions/', include('questions.urls', namespace='questions')),

    
]

    