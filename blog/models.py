from django.db import models

from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


'''
class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
'''


class Blog(models.Model):
    title = models.CharField('标题', max_length=50)
    author = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        verbose_name='作者',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.DO_NOTHING,
        verbose_name='分类',
    )
    content = models.TextField('内容')
    created_time = models.DateTimeField('发布时间', auto_now_add=True)
    modified_time = models.DateTimeField('最近修改', auto_now=True)

    class Meta:
        ordering = [
            '-modified_time',
            '-created_time',
        ]

    def __str__(self):
        return "<Blog: %s>" % self.title