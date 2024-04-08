from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Event, EventType
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
    
    fields = ['type','name','date','start_time', 'end_time', 'description']

class EventUpdateView(UpdateView):
    model = Event
    fields = ['type','name','date','start_time', 'end_time', 'description']
    
class EventDeleteView(DeleteView):
    model = Event
    template_name = "schedrule_app\event_confirm_delete.html"
    success_url = "/events"
