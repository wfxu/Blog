# -*- coding:utf-8 -*-

from django.shortcuts import render
from Model.models import Mes


def search_post(request):
	#  获取表单数据，存储到数据库
	if request.POST:
		text = Mes(message=request.POST['q'])
		text.save()

	# 获取数据库表的所有数据
	list_mes = Mes.objects.all().order_by("-id")
	return render(request, 'message.html', locals())
