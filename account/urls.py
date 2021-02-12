from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('logout/', views.log_out, name='logout'),
    path('register/', views.register, name='register'),

    path('login/<uidb64>/<token>/', views.log_in, name='login'),
]
