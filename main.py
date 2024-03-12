import sqlite3
import random

names = ['Chase Without Fear',
         'Child of The Plague',
         'Turtles of The River',
         'Agent of Joy',
         'Admiring Dreams',
         'Achievement of Yesterday',
         'Agents of The East',
         'Altering the Past',
         'Amusing Dreams',
         'Ancestry with Honor',
         'Angel of Despair',
         'Calling the Jungle',
         'Unity with Determination',
         'Children of Desire',
         'Choice of Gold',
         'Sword of The Night',
         'Symbols in My Leader',
         'Choice of Joy',
         'Cleaning Up the Maze',
         'Traitors Without Courage',
         'Tree of Despair'
         ]

cover_type = ['Softcover',
              'Hardcover with ImageWrap',
              'Hardcover with dust jacket  '
              ]

category = ['Comics',
            'Computers & Tech',
            'Romance',
            'Sports',
            'Teen',
            'Westerns'
            ]

conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute(""" CREATE TABLE BOOKS(
            name text,
            page_quantity int,
            cover_type text,
            category text
            )        
            """)


def calculate_with_python(data):
    print(data)
    arr = [_[1] for _ in data]
    print(f'ყველა წიგნის გვერდების საშუალო რაოდენობა = {sum(arr) / len(data)}')
    max_account = None
    for item in data:
        if item[1] == max(arr):
            max_account = item
    print(f'გვერდების მაქსიმალური რაოდენობის მქონე ჩანაწერია: {max_account}')


for _ in range(0, 10):
    name_choice = random.choice(names)
    names.remove(name_choice)
    page_quantity_choice = random.randint(1, 2500)
    cover_type_choice = random.choice(cover_type)
    category_choice = random.choice(category)
    c.execute('''INSERT INTO BOOKS (name, page_quantity, cover_type, category) VALUES (?, ?, ?, ?)''',
              (name_choice, page_quantity_choice, cover_type_choice, category_choice))

c.execute("SELECT * FROM BOOKS")

calculate_with_python(c.fetchall())
