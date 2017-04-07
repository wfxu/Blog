#  -*- coding:utf-8 -*-

from django.shortcuts import render_to_response, render
from django.db.models import Count, Q
from Model.models import Blog, Mes
from django.db import connection
from django.core.paginator import Paginator
import datetime


# from django.http import HttpResponse

def com():
    # 页面共有部分
    num_category = Blog.objects.values('classify').annotate(dcount=Count('classify'))
    num_time = Blog.objects.extra(select={'month': connection.ops.date_trunc_sql('month', 'toptime')}).values(
        'month').annotate(tcount=Count("topic")).order_by("-month")

    rank_mes = Mes.objects.order_by('-mestime')[:5]
    '''通过游标获取执行语句，获取热评文章.ps：游标返回的是一个包含元祖的列表，元祖为每个字段'''
    rank_blog = {}
    cursor = connection.cursor()
    cursor.execute("SELECT topmes_id FROM model_mes where julianday('now')- julianday(mestime) <30 "
                   "group by topmes_id order by count(message) desc limit 0,5")
    for o in cursor.fetchall():
        for p in o:
            rank_blog[p] = p
    return num_category, num_time, rank_blog, rank_mes


def blog_list(request):
    # 博客列表
    list_blog = Blog.objects.all().order_by("-toptime")
    p=Paginator(list_blog,5)
    #将博客每五个分为一页
    page_x=p.page(1)
    page=page_x.object_list
    page_num=range(1,p.num_pages+1)

    num_category, num_time, rank_blog, rank_mes = com()
    if 'search' in request.GET:
        #搜索后的博客列表
        search_list = Blog.objects.filter(Q(topic__contains=request.GET['search']) | Q(
            content__contains=request.GET['search'])).order_by("-toptime")
        return render(request, "blog_search.html", locals())
    return render_to_response("blog.html", locals())

def blog_list_page(request,pages):
    #翻页后的博客列表
    list_blog = Blog.objects.all().order_by("-toptime")
    p=Paginator(list_blog,5)
    page_x=p.page(pages)
    page=page_x.object_list
    page_num=range(1,p.num_pages+1)
    pages=int(pages)

    num_category, num_time, rank_blog, rank_mes = com()
    if 'search' in request.GET:
        # 搜索后的博客列表
        search_list = Blog.objects.filter(Q(topic__contains=request.GET['search']) | Q(
            content__contains=request.GET['search'])).order_by("-toptime")
        return render(request, "blog_search.html", locals())
    return render_to_response("blog_page.html", locals())

def blog_con(request, title):
    # 博客内容
    if request.POST:
        '''for obj in Blog.objects.filter(topic=title): 就相当于
        Blog.objects.get(topic=title) OR Blog.objects.filter(topic=title).order_by('topic')[0]
        总结：for 循环就是提取出单个对象，所以只要利用“get()”或者利用“排序+切片”提取单个对象就行了'''
        obj = Blog.objects.get(topic=title)  # 提取文章对象PS：因为topmes是外键，所以必须赋值对象，不能赋值数值或字符串
        if Mes.objects.filter(topmes=title).exists():
            # 如果存在评论就楼层递增，如果没有就使用默认值
            obj_f = Mes.objects.filter(topmes=title).order_by('-floor')[0]  # 提取最后评论的楼层
            text = Mes(message=request.POST['q'], topmes=obj, floor=obj_f.floor + 1)
        else:
            text = Mes(message=request.POST['q'], topmes=obj)
        text.save()

    # 获取数据库表的所有数据
    con = Blog.objects.filter(topic=title)
    list_mes = Mes.objects.filter(topmes=title).order_by("-mestime")
    num_category, num_time, rank_blog, rank_mes = com()
    if 'search' in request.GET:
        search_list = Blog.objects.filter(Q(topic__contains=request.GET['search']) | Q(
            content__contains=request.GET['search'])).order_by("-toptime")
        return render(request, "blog_search.html", locals())
    return render(request, "blog_con.html", locals())


def blog_category(request, category):
    # 博客分类列表
    list_blog_category = Blog.objects.filter(classify=category).order_by("-toptime")
    num_category, num_time, rank_blog, rank_mes = com()
    if 'search' in request.GET:
        search_list = Blog.objects.filter(Q(topic__contains=request.GET['search']) | Q(
            content__contains=request.GET['search'])).order_by("-toptime")
        return render(request, "blog_search.html", locals())
    return render(request, "blog_category.html", locals())


def blog_time(request, times):
    # 博客时间线列表
    list_blog_time = {}
    # list_blog_time=Blog.objects.extra(select={'time_month':connection.ops.date_trunc_sql('month','toptime')}).extra(select={'time':times}).order_by("-toptime")
    for i in Blog.objects.extra(select={'time_month': connection.ops.date_trunc_sql('month', 'toptime')}):
        if i.time_month[0:7] == times:
            list_blog_time[i] = Blog.objects.get(topic=i.topic)
    num_category, num_time, rank_blog, rank_mes = com()
    if 'search' in request.GET:
        search_list = Blog.objects.filter(Q(topic__contains=request.GET['search']) | Q(
            content__contains=request.GET['search'])).order_by("-toptime")
        return render(request, "blog_search.html", locals())
    return render(request, "blog_time.html", locals())


def blog_search(request):
    # 搜索功能
    if 'search' in request.GET:
        search_list = Blog.objects.filter(Q(topic__contains=request.GET['search']) | Q(
            content__contains=request.GET['search'])).order_by("-toptime")
    num_category, num_time, rank_blog, rank_mes = com()
    return render(request, "blog_search.html", locals())
