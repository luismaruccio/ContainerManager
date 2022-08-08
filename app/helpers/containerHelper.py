import docker


class ContainerHelper():
    def __init__(self):
        self.client = docker.from_env()

    def does_the_container_exist(self, containername):
        containers = self.client.containers.list(
            all=True)

        containerInstance = None
        for container in containers:
            if container.name == containername:
                containerInstance = container
                break

        if containerInstance == None:
            return None
        else:
            return container

    def stop_container(self, container):
        container.stop()

    def remove_container(self, container):
        container.remove()

    def run_container(self, image, environmentVariables, name, ports):
        environmentList = self.map_environment(environmentVariables)
        portsList = self.map_ports(ports)
        self.client.containers.run(image=image, detach=False, environment=environmentList,
                                   name=name, ports=portsList, restart_policy={"Name": "always"})

    def pull_image(self, image):
        self.client.containers.get(image)

    def map_environment(self, environmentVariables):
        environment = []

        for environmentVariable in environmentVariables:
            environment.append(
                f'{environmentVariable.name}={environmentVariable.value}')

        return environment

    def map_ports(self, ports):
        portsList = dict()

        for port in ports:
            portsList[f'{port.containerport}/{port.protocol}'] = port.value

        return portsList
