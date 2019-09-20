import conf_parser.basic as basic
import base64
import urllib.parse
import requests


class Parser(basic.Parser):
    def node_name(self, url) -> str:
        return urllib.parse.unquote(urllib.parse.urlparse(url).fragment)


class RemoteSubscription(basic.RemoteSubscription):
    def download(self, url: str) -> list:
        return requests.get(self.url).content.decode().splitlines()

    def node_names(self, data: list) -> list:
        parser: Parser = Parser()
        return [parser.node_name(url) for url in data]
