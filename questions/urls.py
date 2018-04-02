
from django.conf.urls import url

from questions import views

app_name = "questions"

urlpatterns = [
	url(r'^$', views.QuestionsList.as_view(), name='questions_list'),


]