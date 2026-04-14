from django.urls import path
from . import views

urlpatterns = [
    path('',views.index), # views.py에 index함수 만들거임
    
]