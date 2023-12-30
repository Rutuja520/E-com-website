# myapp/urls.py

from django.urls import path
from .views import home, about, contact, admin_customer, admin_product, admin_orders

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('admin/customer/', admin_customer, name='admin_customer'),
    path('admin/product/', admin_product, name='admin_product'),
    path('admin/orders/', admin_orders, name='admin_orders'),
]
