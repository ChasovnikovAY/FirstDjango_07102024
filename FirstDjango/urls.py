from django.urls import path
from MainApp import views

urlpatterns = [
    path("", views.home),
    path("about",views.about),
    path("item/<int:item_num>/", views.get_item),
    # path("get_items", views.get_items)

    path("items/", views.items_list, name = "items_list"),
]
