from django.conf import settings
from django.urls import path
from MainApp import views
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home),
    path("about",views.about),
    # path("item/<int:item_num>/", views.get_item),
    # path("get_items", views.get_items)

    path("items/", views.items_list, name="items_list"),
    path("item/<int:item_id>", views.get_item, name="get_item")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
