from django.shortcuts import render, get_object_or_404
from newsy.models import News


def index(request):
    news_list = list(News.objects.order_by('-date', '-posted_hour'))
    for news in news_list:
        news.body_short = '.'.join(news.body.split('.')[:5])
    context = {
        'news_list': news_list,
    }
    return render(request, 'newsy/index.html', context)


def detail(request, permalink):
    news = get_object_or_404(News, id=permalink)
    context = {
        'news': news
    }
    return render(request, 'newsy/detail.html', context)
