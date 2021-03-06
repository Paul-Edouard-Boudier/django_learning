from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db.models import Q

from website.models import IngredientType, CannedFood, Ingredient


def shop(request):
    if request.method == 'POST':
        search = request.POST['canned_search']
        result = CannedFood.objects.filter(
                    Q(ingredients__name__contains=search) | Q(name__contains=search)
                ).distinct().values_list('id', flat=True)
        return JsonResponse(list(result), safe=False)
    else:
        data = {
            'canned_foods': CannedFood.objects.all(),
        }

        return render(request, 'website/shop.html', data)


def product_detail(request, id):
    canned_food = CannedFood.objects.get(pk=id)
    data = {'canned_food': canned_food}
    return render(request, 'website/product_detail.html', data)
