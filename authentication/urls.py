from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from authentication.views import *

urlpatterns = [
    path('', RegisterFormPage.as_view(), name='RegisterFormPage')
]