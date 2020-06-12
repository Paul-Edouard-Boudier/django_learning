from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse

from website.models import CannedFood, Stock


def add_to_cart(request, id):
    """
    add a stock object to the cart
    """
    if request.method != 'GET':
        return HttpResponseRedirect('/boutique')

    product_to_add = get_object_or_404(Stock, pk=id)
    request.session['cart'] = request.session.get('cart', []) + [product_to_add.id]
    item_name = f'{product_to_add.cannedfood.name} {product_to_add.weight}g'

    return JsonResponse({'name': item_name})


def detail(request):
    """
    display the detail of a cart
    """
    data = {}
    if (product_ids := request.session.get('cart', [])):
        products = [s for s in Stock.objects.filter(id__in=product_ids)]
        data['products_in_cart'] = products

    return render(request, 'cart/details.html', data)
