from django.shortcuts import render
from django.http import HttpResponse

items = [
{"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
{"id": 2, "name": "Куртка кожаная" ,"quantity":2},
{"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
{"id": 7, "name": "Картофель фри" ,"quantity":0},
{"id": 8, "name": "Кепка" ,"quantity":124},
]

# Create your views here.
def home(request):
    text = """<h1>Изучаем Django<h1>
    <strong>Часовников А.Ю.</strong>
    """
    return HttpResponse(text)

def about(request):
    text = """
    Фамилия: <b>Часовников</b><br>
    Имя: <b>Алексей</b><br>
    Отчество: <b>Юрьевич</b><br>
    emain: <b>chasovnikov.aleksey@gmail.com<br>
    """
    return HttpResponse(text)

def get_item(request, item_num):
    if item_num in items:
        text = f"товар {item_num}, Имя {items[item_num]}"
    else:
        text = f"Товар с id={item_num} не найден"
    return HttpResponse(text)