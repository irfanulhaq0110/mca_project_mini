from users import views
from django.urls import path
urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('register_driver/',views.register_driver,name='register_driver'),
    path('register_passenger/',views.register_passenger,name='register_passenger'),

]