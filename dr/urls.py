from django.urls import path

from dr import views

urlpatterns = [
    path('dr/', views.drug_entry, name='drug_entry'),
]