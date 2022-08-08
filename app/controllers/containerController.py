import json
from types import SimpleNamespace
from flask_restful import Resource, request

from app.services.containerService import ContainerService


class ContainerController(Resource):
    def __init__(self):
        self.containerService = ContainerService()

    def post(self):
        data = request.get_json(force=True)
        container = json.loads(
            data, object_hook=lambda d: SimpleNamespace(**d))

        return {
            "message": "get: hello from the testcontroller"
        }
