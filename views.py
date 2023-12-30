# myapp/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def admin_customer(request):
    # Your logic for admin customer view
    return render(request, 'admin/customer.html')

def admin_product(request):
    # Your logic for admin product view
    return render(request, 'admin/product.html')

def admin_orders(request):
    # Your logic for admin orders view
    return render(request, 'admin/orders.html')
