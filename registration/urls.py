from django.urls import path
from . import views

urlpatterns=[
    path('index', views.index, name="index"),
    path('index/<slug:fundi_services>', views.services, name="services"),
    path('signup', views.signup, name="signup"),
    path('login', views.login, name='login'),
    path('userlist', views.userlist, name='userlist')
]