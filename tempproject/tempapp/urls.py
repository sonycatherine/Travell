from .import views
from django.urls import path

urlpatterns=[
    path('',views.index,name='demo'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('destinations/', views.destinations, name='destinations'),
    path('contact/', views.contact, name='contact'),
    path('logout/', views.logout, name='logout'),

]

