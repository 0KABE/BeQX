import conf_parser.basic as basic
import requests
import urllib.parse
import base64


class Parser(basic.Parser):
    def node_name(self, url):
        # ssr://netloc -> netloc
        base64_content: str = urllib.parse.urlparse(url).netloc
        # add missing padding
        base64_content += '='*(-len(base64_content) % 4)
        # urlsafe base64 decode
        # decode bytes to str
        # add "ssr://" at the leading
        content: str = "ssr://" + \
            base64.urlsafe_b64decode(base64_content).decode()
        # get parameter dictionary
        param_dict: dict = urllib.parse.parse_qs(
            urllib.parse.urlparse(content).query)
        # replace ' ' by '+'
        remarks = param_dict["remarks"][0].replace(' ', '+')
        # add missing padding
        # get the parameter remarks
        name: str = base64.urlsafe_b64decode(
            remarks+'='*(-len(remarks) % 4)).decode()
        return name


class RemoteSubscription(basic.RemoteSubscription):
    def download(self, url: str) -> list:
        content: bytes = requests.get(self.url).content
        return content.decode().splitlines()

    def node_names(self, data: list) -> list:
        parser: Parser = Parser()
        return [parser.node_name(url) for url in data]
