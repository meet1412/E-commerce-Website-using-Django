from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
import datetime

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        # Create empty cart for now for non-logged-in user
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store/home.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        try:
            cart = json.loads(request.COOKIES['cart'])
        except:
            cart = {}
            print('CART:', cart)

        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
        
        for i in cart:
            try:
                product = Product.objects.get(id=i)
                total = product.price * cart[i]['quantity']
                order['get_cart_total'] += total
                order['get_cart_items'] += cart[i]['quantity']

                item = {
                    'product': {
                        'id': product.id,
                        'name': product.name,
                        'price': product.price,
                        'imageURL': product.imageURL,
                    },
                    'quantity': cart[i]['quantity'],
                    'get_total': total,
                }
                items.append(item)
            except:
                pass    

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items  # Call the method correctly
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']  # Use the dictionary value

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

def processOrder(request):
    import datetime
    import json

    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        # Authenticated user flow
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    else:
        # Guest user flow
        name = data['form']['name']
        email = data['form']['email']

        # Create or retrieve a customer
        customer, created = Customer.objects.get_or_create(email=email)
        customer.name = name
        customer.save()

        # Create a new order for the guest user
        order = Order.objects.create(
            customer=customer,
            complete=False,
        )

        # Add items from the cart to the order
        cart = data.get('cart', {})
        for item_id, item_details in cart.items():
            product = Product.objects.get(id=item_id)
            quantity = item_details['quantity']
            OrderItem.objects.create(order=order, product=product, quantity=quantity)

    # Save transaction details
    order.transaction_id = transaction_id
    if float(data['form'].get('total', 0)) == order.get_cart_total:
        order.complete = True
    order.save()

    # Save shipping information
    shipping_data = data['shipping']
    ShippingAddress.objects.create(
        customer=customer,
        order=order,
        address=shipping_data['address'],
        city=shipping_data['city'],
        state=shipping_data['state'],
        zipcode=shipping_data['zipcode'],
    )

    return JsonResponse('Order processed successfully', safe=False)