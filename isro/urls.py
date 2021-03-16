from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index, name='index'),
    path('card/', CardView.as_view(), name='CardView'),
    path('addSrc/', AddSource.as_view(), name='AddSourceView'),
    path('addPub/', AddPub.as_view(), name='AddPublicationViews'),
]
