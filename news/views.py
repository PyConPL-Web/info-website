from django.shortcuts import render, get_object_or_404
from news.models import News


def index(request):
    news_list = list(News.objects.order_by('-date', '-posted_hour'))
    for news in news_list:
        if len(news.body) < 100:
            news.body_short = news.body
            continue
        end = 100
        news.body_short = news.body[:end]
        while news.body[end] != ' ':
            news.body_short += news.body[end]
            end += 1
        news.body_short += '...'
    context = {
        'news_list': news_list,
    }
    return render(request, 'index.html', context)


def detail(request, permalink):
    news = get_object_or_404(News, id=permalink)
    context = {
        'news': news
    }
    return render(request, 'detail.html', context)
