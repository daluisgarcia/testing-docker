import json

from flask import request

from .database import get_database
from .models import Greetings


def define_routes(app):
    @app.route("/saludos")
    @app.route("/saludos/<id>")
    def greetings_list(id = None):
        if id is None:
            greetings = Greetings.query.all()

            return [greeting.as_dict() for greeting in greetings]

        greeting = Greetings.query.get(id)
        if greeting is None:
            return {
                "error": "Saludo no encontrado"
            }, 404
        
        return greeting.as_dict()

    @app.route("/saludos", methods=["POST"])
    def greetings_create():
        try:
            greeting_data = json.loads(request.data)
            greeting_content = greeting_data.get("mensaje", None)

            if greeting_content is None:
                return {
                    "error": "Contenido no válido"
                }, 400
            
            db = get_database()
            greeting = Greetings(message=greeting_content)
            db.session.add(greeting)
            db.session.commit()

            return {
                "message": "Saludo creado"
            }, 201
        except json.JSONDecodeError:
            return {
                "error": "Contenido no válido"
            }, 400