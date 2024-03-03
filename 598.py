from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from estore.models import Category, Product, Cart
from square.client import Client
import decimal


client = Client(
    access_token='{{ACCESS_TOKEN}}',
    environment='sandbox'
)

LOCATION_ID='{{LOCATION_ID}}'
CUSTOMER_ID = '{{CUSTOMER_ID}}'


def home(request):
    categories = Category.objects.filter()[:3]
    products = Product.objects.filter()[:8]
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'estore/index.html', context)


def category_products(request, url_slug):
    category = get_object_or_404(Category, url_slug=url_slug)
    products = Product.objects.filter(category=category)
    categories = Category.objects.all()
    context = {
        'category': category,
        'products': products,
        'categories': categories,
    }
    return render(request, 'estore/category_products.html', context)


def cart(request):
    cart_products = Cart.objects.all()

    amount = cart_total()
    shipping_amount = decimal.Decimal(0)

    context = {
        'cart_products': cart_products,
        'amount': amount,
        'shipping_amount': shipping_amount,
        'total_amount': amount + shipping_amount
    }
    return render(request, 'estore/cart.html', context)


def cart_total():
    amount = decimal.Decimal(0)
    cart_items = [item for item in Cart.objects.all()]
    if cart_items:
        for item in cart_items:
            temp_amount = (item.quantity * item.product.price)
            amount += temp_amount

    return amount


def add_to_cart(request):
    product_id = request.GET.get('prod_id')
    product = get_object_or_404(Product, id=product_id)

    if cart_total()+product.price < 50000:
        item_already_in_cart = Cart.objects.filter(product=product_id)
        if item_already_in_cart:
            cart_item = get_object_or_404(Cart, product=product_id)
            cart_item.quantity += 1
            cart_item.save()
        else:
            Cart(product=product).save()
    else:
        messages.error(
            request, 'Couldn\'t add item to the cart because orders worth more than $50,000 can\'t be created.')
    return redirect('estore:cart')


def remove_from_cart(request, cart_id):
    if request.method == 'GET':
        c = get_object_or_404(Cart, id=cart_id)
        c.delete()
    return redirect('estore:cart')


def increment_cart(request, cart_id):
    if request.method == 'GET':
        cart_item = get_object_or_404(Cart, id=cart_id)
        if cart_total()+cart_item.product.price < 50000:
            cart_item.quantity += 1
            cart_item.save()
        else:
            messages.error(
                request, 'Couldn\'t increment the quantity because orders worth more than $50,000 can\'t be created.')
    return redirect('estore:cart')


def decrement_cart(request, cart_id):
    if request.method == 'GET':
        cart_item = get_object_or_404(Cart, id=cart_id)
        if cart_item.quantity == 1:
            cart_item.delete()
        else:
            cart_item.quantity -= 1
            cart_item.save()
    return redirect('estore:cart')


def create_order(request):
    body = {
        "order": {
            "location_id": LOCATION_ID,
            "line_items": []
        }
    }

    cart = Cart.objects.all()
    for item in cart:
        newItem = {"name": item.product.title, "quantity": str(item.quantity), "base_price_money": {
            "amount": int(item.product.price*100), "currency": "USD"}}
        body['order']['line_items'].append(newItem)
        item.delete()
    result = client.orders.create_order(body)

    messages.success(
        request, 'The order has been created successfully using the Sqaure API.')
    context = {'order': result.body['order']}
    return render(request, 'estore/order.html', context)


def invoice(request, order_id):
    customer_id = CUSTOMER_ID
    draft_invoice = get_draft_invoice(order_id, customer_id)
    published_invoice = publish_invoice(
        draft_invoice['id'], draft_invoice['version'])

    messages.success(
        request, 'The invoice has been generated successfully using the Sqaure API.')
    context = {'invoice': published_invoice}
    return render(request, 'estore/invoice.html', context)


def get_draft_invoice(order_id, customer_id):
    result = client.invoices.list_invoices(location_id=LOCATION_ID)

    for invoice in result.body['invoices']:
        if invoice['order_id'] == order_id:
            return invoice

    result = client.invoices.create_invoice(
        body={
            "invoice": {
                "order_id": order_id,
                "primary_recipient": {
                    "customer_id": customer_id
                },
                "payment_requests": [{
                    "request_type": "BALANCE",
                    "due_date": "2050-01-14"
                }],
                "delivery_method": "EMAIL",
                "accepted_payment_methods": {
                    "card": True,
                    "square_gift_card": True
                }
            }
        }
    )
    return result.body['invoice']


def publish_invoice(id, version):
    result = client.invoices.publish_invoice(
        invoice_id=id,
        body={"version":  version}
    )
    return result.body['invoice']

