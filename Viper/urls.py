from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload, name='upload'),
    path('contact+us/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    path('order/', views.order_page, name='order'),
    path('medicine/<int:id>/', views.medicine_detail, name='medicine_detail'),

]