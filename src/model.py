from datetime import datetime
from typing import List

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from .db import db


class ProductCategory(db.Model):
    """Категория товара"""
    __tablename__ = 'product_category'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), unique=True)

    products: Mapped[List["Product"]] = relationship(
            back_populates="category", cascade="all, delete-orphan"
    )


class Product(db.Model):
    """Товар"""
    __tablename__ = 'product'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    category_id: Mapped[int] = mapped_column(ForeignKey("product_category.id"))

    category: Mapped['ProductCategory'] = relationship(back_populates="products")

    sales: Mapped[List["Sale"]] = relationship(
            back_populates="product", cascade="all, delete-orphan"
    )


class Sale(db.Model):
    """Продажа"""
    __tablename__ = 'sale'

    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
    count: Mapped[int]
    date: Mapped[datetime] = mapped_column(server_default=func.now())

    product: Mapped['Product'] = relationship(back_populates="sales")
