from flask import Flask

from .config import Config
from .db import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from .blueprints import product, sales
    app.register_blueprint(product.product_bp, url_prefix='/products')
    app.register_blueprint(sales.sales_bp, url_prefix='/sales')

    return app
