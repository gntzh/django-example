from django.shortcuts import render, get_object_or_404
from .models import Blog, Category
from django.views import generic
from django.core.paginator import Paginator
from django.conf import settings

import markdown


def blog_list(request):
    blogs_all = Blog.objects.all()
    paginator = Paginator(blogs_all, settings.PAGINATOR_PER_PAGE)  # 分页
    page_num = request.GET.get('page', 1)  # 获取页面参数(GET)
    page = paginator.get_page(page_num)
    current_page_num = page.number
    # 获取5页循环范围
    page_range = list(
        range(
            max(current_page_num - 2, 1),
            min(paginator.num_pages + 1, current_page_num + 3)))
    # 加上省略标记...
    if current_page_num >= 5:
        page_range.insert(0, '...')
    if current_page_num <= paginator.num_pages - 4:
        page_range.append('...')
    # 加上首页和尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    context = {}
    context['page'] = page
    context['categories'] = Category.objects.all()
    context['page_range'] = page_range
    return render(request, 'blog/blog_list.html', context)


def blog_detail(request, blog_pk):
    blog = get_object_or_404(Blog, pk=blog_pk)
    context = {}
    context['previous_blog'] = Blog.objects.filter(
        modified_time__gt=blog.modified_time).last()
    context['next_blog'] = Blog.objects.filter(
        modified_time__lt=blog.modified_time).first()
    context['blog'] = get_object_or_404(Blog, pk=blog_pk)
    return render(request, 'blog/blog_detail.html', context)


def blog_with_category(request, category_pk):
    category = get_object_or_404(Category, pk=category_pk)
    blogs_all = Blog.objects.filter(category=category)
    paginator = Paginator(blogs_all, settings.PAGINATOR_PER_PAGE)  # 分页
    page_num = request.GET.get('page', 1)  # 获取页面参数(GET)
    page = paginator.get_page(page_num)
    current_page_num = page.number
    # 获取5页循环范围
    page_range = list(
        range(
            max(current_page_num - 2, 1),
            min(paginator.num_pages + 1, current_page_num + 3)))
    # 加上省略标记...
    if current_page_num >= 5:
        page_range.insert(0, '...')
    if current_page_num <= paginator.num_pages - 4:
        page_range.append('...')
    # 加上首页和尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    context = {}
    context['page'] = page
    context['category'] = category
    context['categories'] = Category.objects.all()
    context['page_range'] = page_range
    return render(request, 'blog/blog_with_category.html', context)

'''
class BlogAllFeed(Feed):
    title = "Blog Rsss"
    link = "/blog/"
    description = "ce shi"

    def items(self):
        return Blog.objects.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

    def item_link(self, item):
        return reverse('blog:blog_detail', args=[item.pk])
'''


def blog_detail_md(request, blog_pk):
        blog = get_object_or_404(Blog, pk=blog_pk)
        blog.content_md = markdown.markdown(blog.content, 
                                            extensions=[
                                                'markdown.extensions.extra',
                                                'markdown.extensions.codehilite',
                                                'markdown.extensions.toc',])
        context = {}
        context['blog'] = blog
        return render(request, 'blog/blog_detail_md.html', context)

