from django.urls import path
from bike.views import home
urlpatterns = [
    path('',home,name='home'),
]