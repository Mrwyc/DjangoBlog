import datetime
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from blog.models import *
from datetime import datetime
from django.http import Http404
from utils import pagination


# Create your views here.

def home(request):
    shop_list = BlogsPost.objects.all().order_by('-id')  # 获取全部的Article对象
    current_page = request.GET.get('p', 1)
    current_page = int(current_page)
    page_obj = pagination.Page(current_page, len(shop_list), 10 , 11)
    data = shop_list[page_obj.start:page_obj.end]
    page_str = page_obj.page_str('/blog/home/post_list' % (data))
    return render(request, 'home.html', {'page_str': page_str, 'blog_data': data})


def Test(request):
    return render(request, 'test.html', {'current_time': datetime.now()})


def Detail(request, id):
    try:
        post = BlogsPost.objects.get(id=str(id))
    except BlogsPost.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post': post})


def testpage(requ):
    return render_to_response('home_chajian.html')


def add_article(request):
    return render_to_response('add_wenzhang.html')


