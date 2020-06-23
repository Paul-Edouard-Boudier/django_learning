from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.db.models import F

from django.core.exceptions import ObjectDoesNotExist

from website.models import CannedFood, Stock
from .models import Cart, CartItem


def add_to_cart(request, stock_id: int):
    """
    validate that stock_id is an int and that exist in the range
    of int of ddb maybe


    add a stock object to the cart

    get cart from session
    get product from cart
        if same product already exit, add +1 to quantity
    if product doesn't exist, create new product
        add product to cart

    if doesn't exist, create empty cart
        create and save a product from stock clicked
        add product to cart
    save cart
    """
    if request.method != 'GET':
        return HttpResponseRedirect('/boutique')

    stock_to_add = get_object_or_404(Stock, pk=stock_id)

    if (cart_id := request.session.get('cart_id', None)):
        cart = Cart.objects.get(pk=cart_id)

        try:
            cartitem = CartItem.objects.get(cart__id=cart_id, item__id=stock_id)
            cartitem.quantity += 1
            cartitem.save()
        except ObjectDoesNotExist:
            new_product = CartItem.objects.create(item=stock_to_add)
            cart.cartitems.add(new_product)
    else:
        cart = Cart.objects.create()
        new_product = CartItem.objects.create(item=stock_to_add)
        cart.cartitems.add(new_product)
        request.session['cart_id'] = cart.id

    item_name = f'{stock_to_add.cannedfood.name} {stock_to_add.weight}g'
    total_in_cart = cart.total_items_in_cart
    request.session['total_in_cart'] = total_in_cart

    data = {'result': True, 'name': item_name, 'total': total_in_cart}

    return JsonResponse(data)


def delete_from_cart(request, stock_id):
    """
    validate that stock_id is an int and that exist in the range
    of int of ddb maybe
    """
    if request.method != 'GET':
        return HttpResponseRedirect('/boutique')

    if (cart_id := request.session.get('cart_id', None)):
        cart = Cart.objects.get(pk=cart_id)
        try:
            cartitem = CartItem.objects.get(cart__id=cart_id, item__id=stock_id)
            if cartitem.quantity > 1:
                cartitem.quantity -= 1
                cartitem.save()
            else:
                cart.cartitems.remove(cartitem)
            request.session['total_in_cart'] -= 1
        except ObjectDoesNotExist:
            return JsonResponse({'result': False})

    else:
        return JsonResponse({'result': False})

    if request.META.get('HTTP_REFERER', None) != '/panier':
        return HttpResponseRedirect('/panier')

    item_name = f'{stock_to_add.cannedfood.name} {stock_to_add.weight}g'
    total_in_cart = cart.total_items_in_cart
    request.session['total_in_cart'] = total_in_cart

    data = {'result': True, 'name': item_name, 'total': total_in_cart}

    return JsonResponse(data)


def detail(request):
    # del request.session['cart_id']
    # del request.session['total_in_cart']
    """
    display the detail of a cart
    """
    data = {}
    if (cart_id := request.session.get('cart_id', None)):
        cart = Cart.objects.get(pk=cart_id)
        data['products_in_cart'] = cart.cartitems.all()
        data['total_price'] = cart.cart_price

    return render(request, 'cart/details.html', data)
