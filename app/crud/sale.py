from datetime import datetime

from sqlalchemy import desc
from sqlalchemy.orm import selectinload
from sqlalchemy.sql import func

from app.db import db
from app.model import Product, Sale


def get_count_by_period(start_date: datetime, end_date: datetime) -> int:
    """Получение кол-ва продаж за период

    :param start_date: Дата начала периода
    :param end_date: Дата окончания периода
    :return: Кол-во
    """

    count = (
        db.session.query(func.sum(Sale.count))
        .filter(Sale.date > start_date, Sale.date < end_date)
        .first()
    )
    count = count[0] or 0
    return count


def top_products_by_period(start_date: datetime, end_date: datetime, limit: int) -> list[tuple[Product, int]]:
    """Получение самых продаваемых товаров за период

    :param start_date: Дата начала периода
    :param end_date: Дата окончания периода
    :param limit: Кол-во товаров
    :return: list[Товар, кол-во продаж]
    """

    products = (
        db.session.query(Product, func.sum(Sale.count).label('count'))
        .join(Sale)
        .options(selectinload(Product.category))
        .filter(Sale.date > start_date, Sale.date < end_date)
        .group_by(Product.id)
        .order_by(desc('count'))
        .limit(limit)
        .all()
    )
    return products
