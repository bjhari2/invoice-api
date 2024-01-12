from django.urls import path
from . import views

urlpatterns = [
    path('', views.getAllInvoices), # Route - "/invoices/"
    path('<int:pk>/', views.getInvoiceByID), # Route - "/invoices/<int:pk>/"
    path('allcustomers/', views.getAllCustomers), # Route - "/invoices/allcustomers/"
]