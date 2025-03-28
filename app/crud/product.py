from sqlalchemy.orm import joinedload

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

    product = Product(name=name, category_id=category_id)
    db.session.add(product)
    db.session.commit()
    return product


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
    db.session.add(product)
    db.session.commit()
    return product


def delete(product: Product):
    """Удаление товара"""
    db.session.delete(product)
    db.session.commit()
