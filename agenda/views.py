from django.shortcuts import render
from django.http import Http404
from django.template.response import TemplateResponse
from agenda import models


def index(request):
    all_events = list(models.Event.objects.order_by('-date', '-start_time'))
    context = {'events': all_events}
    response = TemplateResponse(request, 'index.html', context)
    return response


def detail(request, event_id):
    try:
        event = models.Event.objects.get(pk=event_id)
    except models.Event.DoesNotExist:
        raise Http404("No event with given id")
    return render(request, 'detail.html', {'event': event})

