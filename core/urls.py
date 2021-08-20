from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('users',views.users,name='users'),
    path('create_user',views.create_user,name='create_user'),

]
