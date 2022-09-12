# pages/urls.py
from django.urls import path
from .views import HomePageView, AcercadePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AcercadePageView.as_view(), name='about'), # new 
]