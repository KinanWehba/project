from django.urls import path ,include
from . import views
app_name = 'accounts'
urlpatterns = [
    path('app/',views.app ,name= 'app'),

]

