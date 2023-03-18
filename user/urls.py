from django.urls import path
from user.views import profile, UpdateProfile

urlpatterns = [
    path('', profile, name='profile'),
    path('update/<int:pk>', UpdateProfile.as_view(), name='UpdateProfile')
]