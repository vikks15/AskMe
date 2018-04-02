
from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse 
# Create your models here.


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	rating = models.IntegerField(default=0)

class Question(models.Model):
	author = models.ForeignKey(Profile, on_delete = models.CASCADE)
	title = models. CharField(max_length=64)
	text = models.TextField()
	rating = models.IntegerField(default=0)
	created = models.DateTimeField(auto_now_add=True)
	objects = models.Manager()

	def get_absolute_url(self):
		return reverse('questions:questions_detail', args=[self.publish.year,
															self.publish.strftime('%m'),
															self.publish.strftime('%d'),
															self.slug])


class Answer(models.Model):
	author = models.ForeignKey(Profile, on_delete = models.CASCADE)
	question = models.ForeignKey(Question, on_delete = models.CASCADE)
	title = models.CharField(max_length=64)
	text = models.TextField()
	rating = models.IntegerField(default=0)
	created = models.DateTimeField(auto_now_add=True)

class Question_Like(models.Model):
	question = models.ForeignKey(Question, on_delete = models.CASCADE)
	rating = models.IntegerField(default=0)

class Answer_Like(models.Model):
	answer = models.ForeignKey(Answer, on_delete = models.CASCADE)
	rating = models.IntegerField(default=0)

class Tag(models.Model):
	name =  models.CharField(max_length=20)
	question = models.ForeignKey(Question, on_delete = models.CASCADE)
	rating = models.IntegerField(default=0)