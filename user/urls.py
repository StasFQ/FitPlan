from django.urls import path
from user.views import profile

urlpatterns = [
    path('', profile, name='profile')
]