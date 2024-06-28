from flask import Flask

from core.config import config
from core.database import get_database

app = Flask(__name__)
app.config.from_mapping(dict(config))
SQLALCHEMY_DATABASE_URI = f"{config.get('DB_DRIVER', '')}://{config.get('DB_USER', '')}:{config.get('DB_PASS', '')}@{config.get('DB_HOST', '')}:{config.get('DB_PORT', '')}/{config.get('DB_NAME', '')}"
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI

with app.app_context():
    db = get_database(app)
    from core.controllers import define_routes
    define_routes(app)
    db.create_all()