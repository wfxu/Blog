# -*- coding:utf-8 -*-

#  from django.http import HttpResponse
from django.shortcuts import render,render_to_response
from Model.models import Log


def hello(request):
	#首页应用
	return render(request, 'home.html')

def log(request):
	#日志页面应用
	contents=Log.objects.all().order_by('-log_time')
	return render_to_response('log.html',locals() )

def about(request):
	#介绍页面
	return render_to_response('about.html',locals())