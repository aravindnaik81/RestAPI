from django.urls import path
from .views import *
urlpatterns=[
    path('contacts/', contacts_all, name='contact-list'),
    path('contacts/<str:pk>/', update_contact, name='contact-detail'),
]