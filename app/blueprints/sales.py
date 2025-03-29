from datetime import datetime, timedelta

from flask import Blueprint, request

from app import cache, crud
from app.cache import Tables
from app.misc import response

sales_bp = Blueprint('sales', __name__)


@sales_bp.route('/total', methods=['GET'])
@cache.api_decorator([Tables.SALE, Tables.PRODUCT, Tables.PRODUCT_CATEGORY])
def total_sales():
    """Получение кол-ва продаж за период

    :param start_date: Дата начала периода
    :param end_date: Дата окончания периода
    """

    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    if not (start_date and end_date):
        return response(error='Указаны не все параметры (start_date, end_date)')

    try:
        date_format = "%Y-%m-%d"
        start_date = datetime.strptime(start_date, date_format)
        end_date = datetime.strptime(end_date, date_format) + timedelta(days=1)
    except ValueError:
        return response(error='Дата не соответствует формату YYYY-MM-DD')

    sales_count = crud.sale.get_count_by_period(start_date, end_date)

    return response(result=sales_count)


@sales_bp.route('/top-products', methods=['GET'])
@cache.api_decorator([Tables.SALE, Tables.PRODUCT, Tables.PRODUCT_CATEGORY])
def top_products():
    """Получение самых продаваемых товаров за период

    :param start_date: Дата начала периода
    :param end_date: Дата окончания периода
    :param limit: Кол-во товаров
    """

    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    limit = request.args.get('limit', type=int)

    if not (start_date and end_date and limit):
        return response(error='Указаны не все параметры (start_date, end_date, limit)')

    try:
        date_format = "%Y-%m-%d"
        start_date = datetime.strptime(start_date, date_format)
        end_date = datetime.strptime(end_date, date_format) + timedelta(days=1)
    except ValueError:
        return response(error='Дата не соответствует формату YYYY-MM-DD')

    products = crud.sale.top_products_by_period(start_date, end_date, limit)

    return response(
        result=[
            {'product': p.Product.to_dict(),
             'count': p.count}
            for p in products
        ]
    )
