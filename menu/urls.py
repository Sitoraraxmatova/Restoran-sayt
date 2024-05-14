from django.urls import path 
from .views import home,about,booking,contact,menu,service,team,testimonial


urlpatterns=[
    path('',home,name='home_page'),
    path('about/',about,name='about_page'),
    path('booking/',booking,name='booking_page'),
    path('contact/',contact,name='contact_page'),
    path('menu/',menu,name='menu_page'),
    path('service/',service,name='service_page'),
    path('team/',team,name='team_page'),
    path('testimonial/',testimonial,name='testimonial_page')
]