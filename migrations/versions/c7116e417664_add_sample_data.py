"""Add sample data

Revision ID: c7116e417664
Revises: f45451842669
Create Date: 2025-03-28 21:57:02.967859

"""
from datetime import datetime, timedelta
from random import randint
import random
from typing import Sequence, Union

from app import crud
from app.model import Sale


# revision identifiers, used by Alembic.
revision: str = 'c7116e417664'
down_revision: Union[str, None] = 'f45451842669'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


SAMPLE_DATA = {
    'Электроника': [
        'Смартфон',
        'Ноутбук',
        'Наушники',
        'Смарт-часы',
        'Планшет',
        'Телевизор',
        'Камера',
        'Игровая приставка',
        'Монитор',
        'Клавиатура'
    ],
    'Одежда': [
        'Джинсы',
        'Футболка',
        'Куртка',
        'Кроссовки',
        'Шорты',
        'Свитер',
        'Пальто',
        'Шапка'
    ],
    'Книги': [
        'Гарри Поттер и методы рационального мышления',
        '1984',
        'Преступление и наказание',
        'Властелин колец',
        'Мастер и Маргарита',
        'Братья Карамазовы',
        'Пикник на обочине',
        'Алиса в Стране чудес'
    ],
    'Бытовая техника': [
        'Пылесос',
        'Микроволновка',
        'Холодильник',
        'Стиральная машина',
        'Кофемашина',
        'Тостер',
        'Блендер',
        'Фен'
    ],
    'Игрушки': [
        'Лего',
        'Плюшевый мишка',
        'Кукла Барби',
        'Радиоуправляемая машина',
        'Настольная игра',
        'Ручной камень',
        'Пазлы',
        'Конструктор'
    ]
}


def upgrade() -> None:
    """Upgrade schema."""
    products = []

    for category in SAMPLE_DATA:
        category_obj = crud.product_category.create(name=category)
        for product in SAMPLE_DATA[category]:
            product_obj = crud.product.create(name=product, category_id=category_obj.id)
            products.append(product_obj)

    # Популярность разных товаров (why not?)
    random.shuffle(products)
    step = 4 / (len(products) - 1)
    weights = [5 - (i * step) for i in range(len(products))]

    now = datetime.now()
    time = now - timedelta(days=30*6)

    sales = []
    while time < now:
        product = random.choices(products, weights=weights)[0]
        count = random.choices((1, randint(2, 10)), weights=(5, 1))[0]

        sales.append(Sale(product_id=product.id, count=count, date=time))

        time += timedelta(seconds=randint(1, 1000))
    crud.db_bulk_add(sales)


def downgrade() -> None:
    """Downgrade schema."""
