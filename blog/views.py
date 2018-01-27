from django.shortcuts import render, get_object_or_404
from .models import Blog, Category
from django.views import generic
from django.core.paginator import Paginator


def blog_list(request):
    blogs_all = Blog.objects.all()
    paginator = Paginator(blogs_all, 10)
    page_num = request.GET.get('page', 1)  # 获取页面参数(GET)
    page = paginator.get_page(page_num)
    context = {}
    context['page'] = page
    context['categories'] = Category.objects.all()
    return render(request, 'blog/blog_list.html', context)


def blog_detail(request, blog_pk):
    context = {}
    context['blog'] = get_object_or_404(Blog, pk=blog_pk)
    return render(request, 'blog/blog_detail.html', context)


def blog_with_category(request, category_pk):
    context = {}
    category = get_object_or_404(Category, pk=category_pk)
    context['blogs'] = Blog.objects.filter(category=category)
    context['category'] = category
    context['categories'] = Category.objects.all()
    return render(request, 'blog/blog_with_category.html', context)