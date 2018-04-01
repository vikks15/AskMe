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
from django.urls import path, re_path

from questions import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hot', views.hot, name='questions_'),
    url(r'^ask', views.ask, name='ask_question'),
    url(r'^$', views.base, name='questions_index'),
    url(r'^signin', views.signIn, name='signin'),
    url(r'^signup', views.signUp, name='signup'),
    url(r'^settings', views.settings, name='settings'),
    url(r'^question', views.question, name='questionPage'),
    url(r'^tag', views.tag, name='questionPage')    
]

    """path('admin/', admin.site.urls),
    path('', views.base, name='base_questions'),
    path('hot/', views.hot, name='hot_questions'),
    path('tag/', views.tag, name='tag_questions'),
    path('ask/', views.ask, name='ask_question'),
    path('signup/', views.signUp, name='signup'),
    path('settings/', views.settings, name='settings'),
    path('signin/', views.signIn, name='signin')"""