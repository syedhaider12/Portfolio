from django.urls import path
from.import views

urlpatterns = [
   
    path('',views.home, name='main'),
    path('Home',views.home, name='hom'),
    path('Skills',views.skills, name='skils'),
    path('contact',views.contac, name='con'),
    path('service',views.service, name='ser')

    
]
