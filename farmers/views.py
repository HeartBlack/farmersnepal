from cart.cart import Cart
from django.shortcuts import render, redirect, reverse
from django.contrib.sessions.models import Session
from .models import *
from django.http import JsonResponse
from django.contrib.auth.models import User
from .forms import place_order
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import admin

# Create your views here.


def home(request):
    product = reversed(Product.objects.all().order_by('post_date')[:8])
    # popular_product = list(Order_item.objects.all().order_by('-quantity'))
    popular_product = Product.objects.all().order_by('-sales')[:8]
    if request.method == 'POST':
        if request.POST.is_valid():
            username = request.POST['username']
            print(username)
            subscriber = Subscriber.objects.create(email=username)
            subscriber.save()
    return render(request, 'index.html', {
        'product': product,
        "popular_product": popular_product
    })


def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return JsonResponse({"message": len(request.session['cart'])})


@login_required(login_url="login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    try:
        cart.decrement(product=product)

    finally:
        return redirect("cart_detail")


@login_required(login_url="login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


def cart_detail(request):
    # discount = Product.objects.get()
    form = place_order()
    context = {
        'form': form,
    }
    return render(request, 'cart_detail.html', context)


@login_required(login_url="login")
def order_place(request):
    x = request.session['cart']

    for key, value in x.items():
        product_id = (value['product_id'])
        prodct_qty = float((value['quantity']))
        product_price = float(value['price'])        
        total_ammount = prodct_qty * product_price


        pz = Product.objects.get(id=product_id)
        pz.sales = int(pz.sales) + 1
        pz.save()
        data = Order_item.objects.create(product_id=product_id,
                                         quantity=prodct_qty,
                                         total_ammount=total_ammount)
        data.save()

    if request.method == 'POST':
        
        form = place_order(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'home.html')


@login_required(login_url="login")
@permission_required('is_staff')
def order_item(request):
    place_data = Order_item.objects.all()
    item = Place_order.objects.all()
    return render(request, 'dashboard.html', {
        'items': item,
        'place_order': place_data
    })


def allproducts(request):
    all_products = Product.objects.all()

    context = {'all_products': all_products}

    return render(request, 'product.html', context)


def aboutus(request):
    return render(request, 'about.html')


def contactus(request):
    if request.method == "POST":

        username = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        message1 = Contat_us.objects.create(name=username,
                                            email=email,
                                            subject=subject,
                                            message=message)

        message1.save()

    return render(request, 'contact.html')
