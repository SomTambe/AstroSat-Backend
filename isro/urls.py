from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index, name='index'),
    path('card/', CardView.as_view(), name='CardView'),
]
