from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name="index"),
    path('<slug:fundi_services>', views.services, name="services"),
    path('signup', views.signup, name="signup"),
    path('login', views.login, name='login'),
    path('wellcome', views.wellcome, name='wellcome'),
    path('userlist', views.userlist, name='userlist')
]