import sqlite3
from db import db
with open("./img/3d.jpg", "rb") as f:
    m=f.read()
    print(len(m))

connection = sqlite3.connect("data.db")

cursor = connection.cursor()

create_items_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, title text, price real, desc text, type text, img text)"


cursor.execute(create_items_table)
# cursor.execute("INSERT INTO items VALUES ('test', 10.99)")




connection.commit()
connection.close()




def add_all():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    cart = [
            {
              "title": "Калифорния в кунжуте с крабом ",
              "price": 92,
              "desc": "Нежный сыр, огурец с мясом нежного краба...",
              "id": 1,
              "type": "roll"
            },
            {
               "title": "Дакота",
               "price": 145,
               "desc": "Лосось, уsгорь, креветка, авокадо, яп майонез, икра тобико, икра лососьВес: 265 грамм.",
               "id": 2,
               "type": "roll"
            },
             {
                "title": "Сет «Rice max»",
                "price": 280,
                "id": 5,
                "desc": "Акционная цена! Ролл Кокаин, Якудза, Оранж, сушими из лосося и тунца, Тигровый дракон, Икура и Дьябло",
                "type": "set"
                },
            {
                "title": "Сет «ВЕГАН»",
                "price": 699,
                "id": 6,
                "desc":"Aкционная цена! маки с огурцом, маки с авокадо, Ясай-маки (болгарский перец, помидор, авокадо, огурец, такуан, салатный лист), vegan-Калифорния в кунжуте (авокадо, огурец, болгарский перец, такуан), гункан с чукой, 4 шт",
                "type": "set"
            },
            {
                "title": "Удон с курицей",
                "price": 58,
                "id": 8,
                "desc": "Лапша Удон, Куринное филе ,Соус якитори, Овощи....",
                "type": "nudels"

            },
            {
                "title": "Рис, курица, тигровые креветки",
                "price": 109,
                "id": 9,
                "desc":"Рис с курицей и тигровыми креветками.",
                "type": "nudels"
            },
            {
                "title": "«Мисо широ с угрем»",
                "price": 49,
                "id": 13,
                "desc":"рыбный бульен, мисо паста, угорь, гриб шиитаке, водросли вакаме Вес: 300грамм",
                "type": "soup"
            },
            {
                "title": "Суп «Том-Ям»",
                "price": 89,
                "id": 14,
                "desc":"рыбный бульен, кокосовое молоко, лосось, креветки, мидии, гриб шиитаке, соус ким-чи ,водросли вакаме. Вес: 300грамм",
                "type": "soup"
            },
        ]

    query = "INSERT or REPLACE into items VALUES(?, ?, ?, ?, ?, ?)"



    for item in cart:
        cursor.execute(query, (item["id"],item["title"], item["price"], item["desc"], item["type"], "https://ibb.co/h978JZ9"))

    connection.commit()
    connection.close()


add_all()
