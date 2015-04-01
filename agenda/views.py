from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from agenda import models


def index(request):
    all_events = list(models.Event.objects.order_by('-date', '-start_time'))
    context = {'events': all_events}
    response = TemplateResponse(request, 'index.html', context)
    return response