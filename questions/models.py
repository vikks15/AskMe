
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.fields import GenericRelation #reverse relations
from django.contrib.contenttypes.fields import GenericForeignKey #points on different models
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse 
# Create your models here.

class QuestionManager(models.Manager):
	def newest(self):
		return self.all()

	def hottest(self):
		return self.order_by('rating')

	#def search
class TagsManager(models.Manager):
	def newest_by_tag(self, _tag):
		return get_object_or_404(self, name = _tag).questions.all().order_by('creationTime')


	#def hottest_by tag:


class Profile(models.Model):
	avatar = models.ImageField(
		blank = False,
		default = "static/img/avatars/default.png",
		upload_to = 'static/img/avatars/%Y/%m/%d/'

	)
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	rating = models.IntegerField(default=0)

	def __str__(self):
		return self.user.username


class Tag(models.Model):
	name =  models.CharField(max_length=20)
	#question = models.ForeignKey(Question, on_delete = models.CASCADE)
	rating = models.IntegerField(default=0)
	objects = TagsManager()

	def __str__(self):
		return self.name

class Like(models.Model):
	LIKE = 1
	DISLIKE = -1
	VALUES = ((DISLIKE, 'DISLIKE'), (LIKE,'LIKE'))

	author = models.ForeignKey(Profile, null=False, on_delete = models.CASCADE)
	likeOrDislike = models.IntegerField(choices = VALUES, null = False)
	content_type = models.ForeignKey(ContentType, on_delete = models.CASCADE)
	object_id = models.PositiveIntegerField(verbose_name = "id of related object")
	content_object = GenericForeignKey('content_type', 'object_id')
	#objects = LikeManager()

class Question(models.Model):
	author = models.ForeignKey(Profile, on_delete = models.CASCADE)
	title = models. CharField(max_length=64)
	text = models.TextField()	
	creationTime = models.DateTimeField(auto_now_add=True)
	objects = models.Manager()
	tags = models.ManyToManyField(Tag, blank=True, related_name = 'questions')
	likes = GenericRelation(Like, related_query_name='questions')
	rating = models.IntegerField(default=0)

	objects = QuestionManager()

	def get_absolute_url(self):
		return reverse('questions:questions_detail', args=[self.publish.year,
															self.publish.strftime('%m'),
															self.publish.strftime('%d'),
															self.slug])
	#assigning proper name to model objects (for admin panel)
	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-creationTime']
		
class Answer(models.Model):
	author = models.ForeignKey(Profile, on_delete = models.CASCADE, null = False)
	question = models.ForeignKey(Question, on_delete = models.CASCADE, null = False)
	title = models.CharField(max_length = 64, null = True, blank = True) #null for value, blank for forms
	text = models.TextField()
	creationTime = models.DateTimeField(auto_now_add=True)
	likes = GenericRelation(Like, related_query_name = 'answers')
	rating = models.IntegerField(default = 0)
	is_correct = models.BooleanField(default = False)

	#objects = AnswerManager()
	
	def __str__(self):
		return ('Re: ' + self.question.title)


"""class Question_Like(models.Model): #не нужно, нужно в вопросе
	question = models.ForeignKey(Question, on_delete = models.CASCADE)
	rating = models.IntegerField(default=0)


class Answer_Like(models.Model): #в ответе
	answer = models.ForeignKey(Answer, on_delete = models.CASCADE)
	rating = models.IntegerField(default=0)"""