from django.urls import path ,include
from . import views
app_name = 'accounts'
urlpatterns = [
    path('restaurants/',views.restaurants_list ,name='restaurants_list'),

]

