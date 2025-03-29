from flask import Blueprint, request

from app import cache, crud
from app.cache import Tables
from app.misc import response

product_bp = Blueprint('product', __name__)


@product_bp.route('', methods=['GET'])
@cache.api_decorator([Tables.PRODUCT, Tables.PRODUCT_CATEGORY])
def get_products():
    """Получение списка всех товаров"""
    products = crud.product.get_all()

    return response(result=[product.to_dict() for product in products])


@product_bp.route('', methods=['POST'])
@cache.api_decorator([Tables.PRODUCT])
def create_product():
    """Создание нового товара

    :param name: Название
    :param category_id: ID категории
    """

    name = request.args.get('name')
    category_id = request.args.get('category_id', type=int)

    if not crud.product_category.get(category_id):
        return response(error=f'Категория с ID {category_id} не найдена')

    product = crud.product.create(name, category_id)

    return response(result=product.to_dict())


@product_bp.route('/<int:product_id>', methods=['PUT'])
@cache.api_decorator([Tables.PRODUCT])
def update_product(product_id: int):
    """Обновление товара

    :param product_id: ID товара
    :param name: Название
    :param category_id: ID категории
    """

    name = request.args.get('name')
    category_id = request.args.get('category_id', type=int)

    if not (name or category_id):
        return response(error='Не указан name или category_id')
    if category_id and not crud.product_category.get(category_id):
        return response(error=f'Категория с ID {category_id} не найдена')
    if not (product := crud.product.get(product_id)):
        return response(error=f'Товар с ID {product_id} не найден')

    product = crud.product.update(product, name=name, category_id=category_id)

    return response(result=product.to_dict())


@product_bp.route('/<int:product_id>', methods=['DELETE'])
@cache.api_decorator([Tables.PRODUCT, Tables.SALE])
def delete_product(product_id: int):
    """Удаление товара"""
    if not (product := crud.product.get(product_id)):
        return response(error=f'Товар с ID {product_id} не найден')

    crud.product.delete(product)

    return response(result='Товар успешно удалён')
