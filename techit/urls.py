from django.urls import path,include
from.import views

app_name='techit'

urlpatterns = [
    path('',views.home,name='home'),
    path('contact/',views.contact,name='contact_from'),
    path('about_us/',views.about,name='about'),
    
]
