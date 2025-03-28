from app.db import db
from app.model import ProductCategory


def get(id: int) -> ProductCategory:
    """Получение категории товара по ID"""
    return db.session.query(ProductCategory).filter(ProductCategory.id == id).first()
