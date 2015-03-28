from django.shortcuts import render, get_object_or_404
from news.models import News


def index(request):
    news_list = list(News.objects.order_by('-date', '-posted_hour'))
    for news in news_list:
        news.body_short = '.'.join(news.body.split('.')[:5])
    context = {
        'news_list': news_list,
    }
    return render(request, 'news/index.html', context)


def detail(request, permalink):
    news = get_object_or_404(News, id=permalink)
    context = {
        'news': news
    }
    return render(request, 'news/detail.html', context)
