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

def get_item(request, item_id):
    one_item = Item.objects.get(id=item_id)
    context = { "item":one_item,
                "colors": one_item.colors.all()}
    return render(request, "item.html", context)


def items_list(request):
    item_list = Item.objects.all()
    return render(request,"get_items.html", { "items": item_list} )
