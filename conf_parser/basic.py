import abc


class Parser(object):
    @abc.abstractmethod
    def node_name(self, url: str) -> str:
        pass


class RemoteSubscription(object):
    def __init__(self, url: str):
        self.url: str = url
        self.nodes: list = self.node_names(self.download(url))

    @abc.abstractmethod
    def download(self, url: str) -> list:
        pass

    @abc.abstractmethod
    def node_names(self, data: list) -> list:
        pass
