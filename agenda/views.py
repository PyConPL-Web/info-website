from django.shortcuts import render
from django.template.response import TemplateResponse
from agenda.models import Event
from django.shortcuts import get_object_or_404

def index(request):
    all_events = list(Event.objects.order_by('-date', '-start_time'))
    context = {'events': all_events}
    response = TemplateResponse(request, 'index.html', context)
    return response


def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'detail.html', {'event': event})

