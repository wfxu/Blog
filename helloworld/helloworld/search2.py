# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.template.context_processors import csrf

#����POST��������
def search_post(request):
	ctx={}
	ctx.update(csrf(request))
	if request.POST:
		ctx['rlt']=request.POST['q']
	return render(request,"post.html",ctx)