# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# from tinymce.models import HTMLField
# from ckeditor.fields import RichTextField
from DjangoUeditor.models import UEditorField


# Create your models here.

class Category(models.Model):
	name = models.CharField(u"类型名称", max_length=20, primary_key=True)

	def __unicode__(self):
		return self.name


class State(models.Model):
	name = models.CharField(u"状态名称", max_length=20, primary_key=True)

	def __unicode__(self):
		return self.name


class Blog(models.Model):
	topic = models.CharField(u"标题", max_length=50, primary_key=True)
	digest = models.CharField(u"摘要", max_length=1000)
	classify = models.ForeignKey(Category)
	status = models.ForeignKey(State, default="publication")
	toptime = models.DateTimeField(u"时间", auto_now_add=True)
	content = UEditorField(u"文章")

	def __unicode__(self):
		return self.topic


class Mes(models.Model):
	message = models.CharField(u"信息", max_length=500)
	mestime = models.DateTimeField(u"时间", auto_now_add=True)
	topmes = models.ForeignKey(Blog)
	floor = models.IntegerField(u"楼层", default=1)

	def __unicode__(self):
		return self.message

class Log(models.Model):
	log_content = UEditorField(u"日志内容")
	log_time = models.DateTimeField(u"时间", auto_now_add=True)



from django.db import models

# Create your models here.
