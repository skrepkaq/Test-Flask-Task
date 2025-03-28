from sqlalchemy.orm import joinedload

from app.crud.base import db_add, db_delete
from app.db import db
from app.model import Product


def get(id: int) -> Product:
    """Получение товара по ID"""
    return db.session.query(Product).filter(Product.id == id).first()


def get_all() -> list[Product]:
    """Получение всех товаров"""
    return db.session.query(Product).options(joinedload(Product.category)).all()


def create(name: str, category_id: int) -> Product:
    """Создание товара

    :param name: Название
    :param category_id: ID категории
    :return: Товар
    """

    return db_add(Product(name=name, category_id=category_id))


def update(product: Product, name: str | None = None, category_id: int | None = None) -> Product:
    """Обновление товара

    :param product: Товар
    :param name: Название
    :param category_id: ID категории
    :return: Товар
    """
    if name:
        product.name = name
    if category_id:
        product.category_id = category_id

    return db_add(product)


def delete(product: Product):
    """Удаление товара"""
    db_delete(product)
