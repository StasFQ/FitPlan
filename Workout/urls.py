from django.urls import path

from Workout.views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('trainings/', trainings, name='trainings'),
    path('trainers/', trainers, name='trainers'),
    path('add_train/', CreateTraining.as_view(), name='CreateTraining'),
    path('contact/', contact, name='contact')
]
