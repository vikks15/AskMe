# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Profile, Question, Answer, Tag, Answer_Like, Question_Like

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	pass

@admin.register(Question)
class ProfileAdmin(admin.ModelAdmin):
	pass

@admin.register(Answer)
class ProfileAdmin(admin.ModelAdmin):
	pass

@admin.register(Question_Like)
class ProfileAdmin(admin.ModelAdmin):
	pass

@admin.register(Answer_Like)
class ProfileAdmin(admin.ModelAdmin):
	pass

@admin.register(Tag)
class ProfileAdmin(admin.ModelAdmin):
	pass

