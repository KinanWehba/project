from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.
def restaurants_list(request):
    restaurants = User.objects.all()
    
    return render(request ,'user/restaurants_list.html',{
        'restaurants' : restaurants,
        })


def restaurants_detail(request,slug):
    restaurants_detail = Profile.objects.get(slug=slug)
    
    return render(request ,'user/restaurants_detail.html',{
        'restaurants_detail' : restaurants_detail,
        })
