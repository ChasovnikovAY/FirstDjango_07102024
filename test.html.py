items = [
{"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
{"id": 2, "name": "Куртка кожаная" ,"quantity":2},
{"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
{"id": 7, "name": "Картофель фри" ,"quantity":0},
{"id": 8, "name": "Кепка" ,"quantity":124},
]

cnt = {"id": 1, "name": "Кроссовки abibas" ,"quantity":5}
print(cnt["id"])
print("---------------")
content = { "item_list":items }
for c in content.items():
    print(c)