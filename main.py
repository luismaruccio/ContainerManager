from flask import Flask
from flask_restful import Api

from app.controllers.containerController import ContainerController

app = Flask(__name__)
api = Api(app)
api.add_resource(ContainerController, '/runcontainer')

if __name__ == "__main__":
    app.run(port=5000, debug=True)
