import abc


class Parser(object):
    @abc.abstractmethod
    def node_name(self, url: str) -> str:
        pass


class RemoteSubscription(object):
    def __init__(self, url: str):
        self.url: str = url
        self.nodes: list = self._node_names(self._download(url))

    @abc.abstractmethod
    def _download(self, url: str) -> list:
        pass

    @abc.abstractmethod
    def _node_names(self, data: list) -> list:
        pass
