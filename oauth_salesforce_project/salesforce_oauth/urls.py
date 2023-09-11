from django.urls import path
from . import views

urlpatterns = [
    path('homepage',views.homepage, name='homepage'),
    path('login/', views.login_with_salesforce, name='login_with_salesforce'),
    path('callback/', views.salesforce_callback, name='salesforce_callback'),
    path('logout/', views.logout, name='logout'),
]