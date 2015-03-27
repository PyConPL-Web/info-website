from django.contrib import admin
from agenda.models import Event
from agenda.forms import EventAdminForm


class EventAdmin(admin.ModelAdmin):
    form = EventAdminForm

admin.site.register(Event, EventAdmin)
