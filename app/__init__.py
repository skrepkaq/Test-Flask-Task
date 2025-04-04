import os

from alembic import command
from alembic import config as alembic_config
from flask import Flask

from app.config import Config
from app.db import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from .blueprints import product, sales
    app.register_blueprint(product.product_bp, url_prefix='/api/products')
    app.register_blueprint(sales.sales_bp, url_prefix='/api/sales')

    return app


def run_migrations(app: Flask):
    with app.app_context():
        alembic_cfg = alembic_config.Config(os.path.join(os.path.dirname(__file__), '../alembic.ini'))

        command.upgrade(alembic_cfg, 'head')
