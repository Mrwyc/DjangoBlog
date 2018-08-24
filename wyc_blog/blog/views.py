import datetime
from django.shortcuts import render, render_to_response, redirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import HttpResponse
from blog.models import *
from datetime import datetime
from django.http import Http404
from utils import pagination


# Create your views here.

def home(request):
    shop_list = BlogsPost.objects.all().order_by('-id')  # 获取全部的Article对象
    txt_class = BlogCtg.objects.all().order_by('-id')
    current_page = request.GET.get('p', 1)
    current_page = int(current_page)
    page_obj = pagination.Page(current_page, len(shop_list), 10 , 11)
    data = shop_list[page_obj.start:page_obj.end]
    page_str = page_obj.page_str('/blog/home/post_list' % (data))
    return render(request, 'home.html', {'page_str': page_str, 'blog_data': data, 'txt_class': txt_class})


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

from blog import form
def add_article(request):
    obj = form.Class_Text()

    return render(request, 'add_wenzhang.html', {'obj':obj})


@csrf_protect
def classification(request):
    if request.method == 'POST':
        name = request.POST['class_name']
        if name:
            BlogCtg.objects.create(**{'name': name})
    return redirect('/blog/home/')


