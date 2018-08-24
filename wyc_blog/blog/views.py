import datetime
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from blog.models import *
from datetime import datetime
from django.http import Http404


# Create your views here.

def home(request):
    post_list = BlogsPost.objects.all()  # 获取全部的Article对象
    return render(request, 'home.html', {'post_list': post_list})


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