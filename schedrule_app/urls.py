from django.urls import path
from . import views
from .views import EventListView 

urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
path('', views.index, name='index'),
path("events/", EventListView.as_view(), name= 'events'),
path('events/<int:pk>', views.EventDetailView.as_view(), name='event-detail'),
path("events/create/", views.EventCreateView.as_view(), name='create-event'),
path('events/<int:pk>/update', views.EventUpdateView.as_view(), name= 'update-event'), 
path('events/<int:pk>/delete', views.EventDeleteView.as_view(), name= 'delete-event'), 
]

