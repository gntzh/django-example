from django.shortcuts import render, get_object_or_404
from .models import Blog, Category
from django.views import generic


def blog_list(request):
    context = {}
    context['blogs'] = Blog.objects.all()
    return render(request, 'blog/blog_list.html', context)


'''
class Blog_listView(generic.ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'
'''


def blog_detail(request, blog_pk):
    context = {}
    context['blog'] = get_object_or_404(Blog, pk=blog_pk)
    return render(request, 'blog/blog_detail.html', context)


def blog_with_category(request, category_pk):
    context = {}
    category = get_object_or_404(Category, pk=category_pk)
    context['blogs'] = Blog.objects.filter(category=category)
    context['category'] = category
    return render(request, 'blog/blog_with_category.html', context)