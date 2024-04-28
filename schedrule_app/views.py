from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Event, EventType, Manager
from .forms import SignupForm, LoginForm, ManagerForm
from datetime import datetime
from django.utils.safestring import mark_safe
from django.contrib import auth,messages
from django.forms import inlineformset_factory
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin

from .utils import Calendar
# Create your views here.
def index(request):
    return render( request, 'schedrule_app/index.html')

def registerPage(request):
    form = SignupForm
    
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='manager')
            user.groups.add(group)
            manager = Manager.objects.create(user=user)
            manager.name = username
            manager.save()
    
            
            messages.success(request, "Account was created for " + username)
            return redirect('login')

    context ={'form':form}
    return render(request,'schedrule_app/register.html',context)


@login_required(login_url='login')
def userPage(request):
    manager = request.user.manager
    form = ManagerForm(instance=manager)
    print("This is the manager page")
    if request.method == 'POST':
        form = ManagerForm(request.POST, request.FILES, instance=manager)
        if form.is_valid():
            form.save()
    context= {'form':form}
    return render(request, 'schedrule_app/user,html',context)

    

            
            
class EventListView(ListView):
    model = Event
    context_object_name = 'events'

class EventDetailView(DetailView):
    model = Event
    
class EventCreateView(LoginRequiredMixin,CreateView):
    model = Event
    fields = ['type','name','start_date_time', 'end_date_time', 'description']
    login_url = "/accounts/login"
    success_url = "/events"

class EventUpdateView(LoginRequiredMixin,UpdateView):
    model = Event
    template_name = "schedrule_app\event_update_form.html"
    login_url = "/accounts/login"
    fields = ['type','name','start_date_time', 'end_date_time', 'description']
    
class EventDeleteView(LoginRequiredMixin,DeleteView):
    model = Event
    template_name = "schedrule_app\event_confirm_delete.html"
    login_url = "/accounts/login"
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