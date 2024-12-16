from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
     products = Product.objects.all()
     context = {'products': products}
     return render(request, 'store/home.html', context)

def cart(request):
     if request.user.is_authenticated:
       customer = request.user.customer 
       order, created = Order.objects.get_or_create(customer=customer, complete=False) 
       items = order.orderitem_set.all()
     
     else:
       items = []
	      
     context = {'items':items, 'order':order}

     return render(request, 'store/cart.html', context)

def checkout(request):
  customer = request.user.customer 
  order, created = Order.objects.get_or_create(customer=customer, complete=False) 
  items = order.orderitem_set.all()
	      
  context = {'items':items, 'order':order}

  return render(request, 'store/checkout.html', context)