from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('search/', views.search, name="search-result"),
    path('doctors/', views.doctors, name="doctors"),
    path('hospitals/', views.hospitals, name="hospitals"),
    path('services/', views.services, name="services"),
    path('medicines/', views.medicines, name="medicines"),
    path('posts/', views.posts, name="posts"),
    path('contact/', views.contact, name="contact"),
    path('hospital/<int:pk>', views.organizationDetail, name='organization-detail'),    
    path('service/<int:pk>', views.serviceDetail, name='service-detail'),    
    path('doctor/<int:pk>', views.doctorDetail, name='doctor-detail')    
]