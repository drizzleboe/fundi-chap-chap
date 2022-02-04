from django.shortcuts import render
from django.http import HttpResponse
from .models import users,region
from .form import signups,sign_in,location,service,image

# Create your views here.
def index(request):
    user  =  users.objects.all()
    _region =  region.objects.all()
    
    return render(request, 'registration/index.html',{
        'register':True,
        'users':user,
        'region':_region
    })
def services(request, fundi_services):
    try:
        details = users.objects.get(slug = fundi_services)
        return render(request, 'registration/services.html',{
        'available':True,
        'user':details      
        })
    except:
        return render(request, 'registration/services.html',{
        'available':False
        })

def signup(request):
    client=users.objects.all()
    form=signups()
    loc=location()
    ser=service()
    img=image()
    return render(request, 'registration/signups.html',{
        'client':client,
        'form':form,
        'location':loc,
        'service':ser,
        'image':img
    })
def userlist(request):
    user  = users.objects.all()
    addre = address.objects.all()
    return render(request, 'registration/userlist.html',{
        'users':user,
        'addre':addre
    })
def login(request):
    signin_form = sign_in()
    return render(request, 'registration/login.html',{
        'signin_form':signin_form,
        
    })