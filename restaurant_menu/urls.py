from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('item/<int:item_id>', views.details, name='details'),
    path('item/add', views.add_item, name='add_item'),
    path('item/<int:item_id>/edit', views.edit_item, name='edit_item'),
    path('item/<int:item_id>/delete', views.delete_item, name='delete_item'),
]

