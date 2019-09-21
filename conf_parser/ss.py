import base64
import urllib.parse

import requests

import conf_parser.basic as basic


class Parser(basic.Parser):
    def node_name(self, url) -> str:
        return urllib.parse.unquote(urllib.parse.urlparse(url).fragment)


class RemoteSubscription(basic.RemoteSubscription):
    def _download(self, url: str) -> list:
        return requests.get(self.url).content.decode().splitlines()

    def _node_names(self, data: list) -> list:
        parser: Parser = Parser()
        return [parser.node_name(url) for url in data]
