from django.urls import path
from .views import *

urlpatterns = [
    path('',login,name='login'),
    path('base/',home,name='home'),
    path('listings/',listings,name='listpage'),
    path('getdata/',get_data,name='getpage'),
    path('update/<id>',update,name='updatepage'),
    path('dashboard/',dashbord,name='dashboardpage'),
    path('appoinments/',appoinments,name='apointmentpage'),
    path('reviews/',reviews,name='reviewspage'),
    path('settings/',settings,name='settingspage'),
    path('visitors/',visitors,name='visitorspage'),
    path('website',website,name='websitepage'),






]