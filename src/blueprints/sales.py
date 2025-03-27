from flask import Blueprint

sales_bp = Blueprint('sales', __name__)


@sales_bp.route('/total', methods=['GET'])
def total_sales():
    """Получить сумму продаж за период

    :param start_date: Дата начала периода
    :param end_date: Дата окончания периода
    """
    pass


@sales_bp.route('/top-products', methods=['GET'])
def top_products():
    """Получить топ-N самых продаваемых товаров за период

    :param start_date: Дата начала периода
    :param end_date: Дата окончания периода
    :param limit: Кол-во товаров
    """
    pass
