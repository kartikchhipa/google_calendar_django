from django.urls import path, include
from rest.views import GoogleCalendarInitView, GoogleCalendarRedirectView, home, events, logout_view

urlpatterns = [
    path('rest/v1/calendar/init/', GoogleCalendarInitView, name='init'),
    path('',home,name='home'),
    path('rest/v1/calendar/redirect/', GoogleCalendarRedirectView, name='redirect'),
    path('events/', events, name='events'),
    path('logout/', logout_view, name='logout_view'),
]
