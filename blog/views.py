from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone

from .models import Article


# Create your views here.
def index(request):
    latest_articles_list = Article.objects.order_by('-pub_date')
    return render(request, 'blog/list.html', {'latest_articles_list': latest_articles_list})


def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Article was not founded!")

    latest_comments_list = a.comment_set.order_by('-id')[:10]

    return render(request, 'blog/detail.html', {'article': a, 'latest_comments_list': latest_comments_list})


def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Article was not founded!")

    a.comment_set.create(author_name=request.POST['name'], comment_text=request.POST['text'], pub_date=timezone.now())

    return HttpResponseRedirect(reverse("blog:detail", args=(a.id,)))


def boot(request):
    return render(request, 'blog/boot.html')
