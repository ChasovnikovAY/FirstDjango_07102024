from typing import ItemsView

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from MainApp.models import Item

# items = [
# {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
# {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
# {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
# {"id": 7, "name": "Картофель фри" ,"quantity":0},
# {"id": 8, "name": "Кепка" ,"quantity":124},
# ]

# Create your views here.
def home(request):
    context = {
        "name": "Часовников Алексей Юрьевич",
        "email": "my_email@mail.ru"
    }
    return render(request, "index.html", context)

def about(request):
    text = """
    Фамилия: <b>Часовников</b><br>
    Имя: <b>Алексей</b><br>
    Отчество: <b>Юрьевич</b><br>
    emain: <b>chasovnikov.aleksey@gmail.com<br>
    """
    return HttpResponse(text)

def get_item(request, item_num):
    item = filter(lambda x: x['id'] == item_num, items)
    if len(list(item)) > 0:
        return render(request, "task2_1.html", next(item))
    return HttpResponseNotFound(f"Товар с номером {item_num} не найден")

def get_items(request):
    # text = ""
    # for i in items:
    item = Item.objects.all()
    #     text += f"<a href='/item/{i['id']}/'>{i['name']} {str(i['quantity'])} штук </a><br>"
    return render(request,"get_items.html", { "items": items} )
    #return HttpResponse(text)