from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .views import EventListView 

urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
path('', views.CalendarView.as_view(), name='calendar'),
path('user/', views.userPage, name ='user_page'),
path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
path('accounts/register/', views.registerPage, name = 'register_page') ,
path('accounts/', include('django.contrib.auth.urls')),
path("calendar/", views.CalendarView.as_view(), name='calendar'),
path("events/", EventListView.as_view(), name= 'events'),
path('events/<int:pk>', views.EventDetailView.as_view(), name='event-detail'),
path("events/create/", views.EventCreateView.as_view(), name='create-event'),
path('events/<int:pk>/update', views.EventUpdateView.as_view(), name= 'update-event'), 
path('events/<int:pk>/delete', views.EventDeleteView.as_view(), name= 'delete-event'),
]

