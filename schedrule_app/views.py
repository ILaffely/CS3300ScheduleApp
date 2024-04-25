from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Event, EventType
from datetime import datetime
from django.utils.safestring import mark_safe

from .utils import Calendar
# Create your views here.
def index(request):
    return render( request, 'schedrule_app/index.html')

class EventListView(ListView):
    model = Event
    context_object_name = 'events'

class EventDetailView(DetailView):
    model = Event
    
class EventCreateView(CreateView):
    model = Event
    fields = ['type','name','start_date_time', 'end_date_time', 'description']
    success_url = "/events"

class EventUpdateView(UpdateView):
    model = Event
    fields = ['type','name','start_date_time', 'end_date_time', 'description']
    
class EventDeleteView(DeleteView):
    model = Event
    template_name = "schedrule_app\event_confirm_delete.html"
    success_url = "/events"

class CalendarView(ListView):
    model = Event
    template_name = 'schedrule_app\calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()