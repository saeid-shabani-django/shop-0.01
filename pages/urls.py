from django.urls import path
from . import views


urlpatterns = [
    path('',views.HomePage.as_view(),name='home'),
    path('about/',views.AboutUs.as_view(),name='about'),
    ]


