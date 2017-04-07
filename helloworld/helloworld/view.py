# -*- coding=utf-8 -*-
#from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
	context={}
	context['hello']='hello world! 世界和平'
	return render(request,'hello.html',context)