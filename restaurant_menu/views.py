from django.shortcuts import render, redirect
from .models import MenuItem, MEAL_TYPE
from django.contrib.auth.decorators import login_required
from .forms import MenuItemForm
from django.contrib import messages


def index(request):
    item_list = MenuItem.objects.all()
    context = {
        'item_list': item_list,
        'item_types': MEAL_TYPE,
    }
    return render(request, "index.html", context)


def details(request, item_id):
    item = MenuItem.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    return render(request, "details.html", context)


@login_required
def add_item(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['author'].username
            item = form.cleaned_data['meal']
            messages.success(request, message=f"Hi {name}, The item {item} is added in the menu!")

    else:
        form = MenuItemForm()
    return render(request, 'add_item.html', {'form': form, })


@login_required
def edit_item(request, item_id):
    instance = MenuItem.objects.get(pk=item_id)

    if request.method == "POST":
        form = MenuItemForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('restaurant_menu:home')

    else:
        form = MenuItemForm(instance=instance)
    return render(request, 'edit_item.html', {'form': form, })


@login_required
def delete_item(request, item_id):
    item = MenuItem.objects.get(pk=item_id)

    if request.method == "POST":
        item.delete()
        return redirect("restaurant_menu:home")

    else:
        return render(request, 'delete_item.html', {'item': item,})
