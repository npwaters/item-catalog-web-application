import sys
import random
from app import session, Base, engine
from category.models import Category
from catalog_item.models import CatalogItem
from user.models import User

Base.metadata.create_all(engine)

with open("catalog_data.txt") as data_source:
    lines = data_source.readlines()

users = [
    User(name="Billy Bob", email="billybob@email.local"),
    User(name="John Citizen", email="jcitizen@email.local")
]

current_category = None
user = None
category_number = 1

for line in lines:
    line_items = [l.rstrip() for l in line.split("|")]
    if len(line_items) == 1:
        if category_number % 2 != 0:
            user = users[0]
        else:
            user = users[1]
        category_number += 1
        current_category = Category(
            name=line_items[0],
            user=user
        )
        session.add(current_category)
        session.commit()
    if len(line_items) > 1:
        catalog_item = CatalogItem(
            name=line_items[0],
            description=line_items[1],
            category=current_category,
            user=user
        )
        session.add(catalog_item)
        session.commit()


sys.exit()
