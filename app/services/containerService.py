from app.helpers.containerHelper import ContainerHelper


class ContainerService():
    def __init__(self):
        self.containerHelper = ContainerHelper()

    def runcontainer(self, container):
        containerInstance = self.containerHelper.does_the_container_exist(
            container.name)

        if containerInstance != None:
            if containerInstance.stats == 'running':
                self.containerHelper.stop_container(containerInstance)

            self.containerHelper.remove_container(containerInstance)

        self.containerHelper.pull_image(container.image)

        self.containerHelper.run_container(container.image, container.environmentVariables,
                                           container.name, container.ports)
