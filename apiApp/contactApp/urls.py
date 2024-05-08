from django.urls import path

urlpatterns=[
    path('contacts/',views.contact_list),
    path('contact/<str:pk>',views.contact_deatils),
]