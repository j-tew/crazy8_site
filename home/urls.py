from django.urls import path

from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('menu/', MenuView.as_view(), name='menu'),
    path('events/', EventView.as_view(), name='events'),
    path('photos/', PhotoView.as_view(), name='photos'),
]