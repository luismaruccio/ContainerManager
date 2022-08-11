from flask_restful import Resource, request
from app.services.containerService import ContainerService


class ContainerController(Resource):
    def __init__(self):
        self.containerService = ContainerService()

    def post(self):
        data = request.get_json()

        container = self.containerService.mapContainer(data)

        self.containerService.runcontainer(container)

        return {
            "message": "Success"
        }
