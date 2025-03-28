from app.crud.base import db_add
from app.db import db
from app.model import ProductCategory


def get(id: int) -> ProductCategory:
    """Получение категории товара по ID"""
    return db.session.query(ProductCategory).filter(ProductCategory.id == id).first()


def create(name: str) -> ProductCategory:
    """Создание категории товара

    :param name: Название
    :return: Категория товара
    """

    return db_add(ProductCategory(name=name))
