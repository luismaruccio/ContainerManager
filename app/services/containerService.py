from app.helpers.containerHelper import ContainerHelper
from app.models.container import Container
from app.models.ports import Ports


class ContainerService():
    def __init__(self):
        self.containerHelper = ContainerHelper()

    def mapContainer(self, json):
        container = Container()
        container.containerName = json.get("containername")
        container.image = json.get("image")

        if json.get("ports") != None:
            portslist = json.get("ports")
            for port in portslist:
                portInstance = Ports()
                portInstance.containerPort = port.get("containerport")
                portInstance.protocolPort = port.get("protocolport")
                portInstance.externalPort = port.get("externalport")
                container.ports.append(portInstance)
        return container

    def runcontainer(self, container):
        RUNNING = "running"
        print("Iniciando")
        containerInstance = self.containerHelper.does_the_container_exist(
            container.containerName)

        print(containerInstance)

        if containerInstance != None:
            print(containerInstance.status)
            if containerInstance.status == RUNNING:
                self.containerHelper.stop_container(containerInstance)

            self.containerHelper.remove_container(containerInstance)

        print("Iniciando Pull Image")
        self.containerHelper.pull_image(container.image)

        print("Iniciando Run Container")
        self.containerHelper.run_container(container.image, container.environmentVariables,
                                           container.containerName, container.ports)
