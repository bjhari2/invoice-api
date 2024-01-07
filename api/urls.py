from django.urls import path
from . import views

urlpatterns = [
    path('', views.getAllInvoices),
    path('<int:pk>/', views.getInvoiceByID),
    path('allcustomers/', views.getAllCustomers),
]