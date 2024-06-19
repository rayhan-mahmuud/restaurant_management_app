from django.shortcuts import render
from .models import MenuItem, MEAL_TYPE


def index(request):
    item_list = MenuItem.objects.all()
    context = {
        'item_list': item_list,
        'item_types': MEAL_TYPE,
    }
    return render(request, "index.html",context)


def details(request, item_id):
    item = MenuItem.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    return render(request, "details.html", context)


