from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def restaurants_list(request):
    restaurants = User.objects.all()
    
    return render(request ,'user/restaurants_list.html',{
        'restaurants' : restaurants,
        })
