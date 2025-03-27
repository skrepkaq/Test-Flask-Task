from flask import Blueprint

product_bp = Blueprint('product', __name__)


@product_bp.route('', methods=['GET'])
def get_products():
    """Получить список всех продуктов"""
    pass


@product_bp.route('', methods=['POST'])
def create_product():
    """Создать новый продукт"""
    pass


@product_bp.route('/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """Обновить продукт"""
    pass


@product_bp.route('/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Удалить продукт"""
    pass
