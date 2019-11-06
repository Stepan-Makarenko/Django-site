import datetime
from django.db import models
from django.utils import timezone


# Create your models here.
class Article(models.Model):
    article_title = models.CharField("Название статьи", max_length=100)
    article_annotation = models.CharField("Аннотация статьи", max_length=1000)
    article_text = models.TextField("Текст статьи")
    author_name = models.CharField('Имя автора', max_length=50)
    pub_date = models.DateTimeField('Дата статьи')

    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('Имя автора', max_length=50)
    comment_text = models.CharField('Текст комментария', max_length=200)
    pub_date = models.DateTimeField('Дата комментария')

    def __str__(self):
        return self.author_name