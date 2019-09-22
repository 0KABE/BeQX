import json
from enum import Enum
from typing import Dict, List, Union

import requests

import sub_parser.ss_sub_parser as ss_sub_parser
import sub_parser.ssr_sub_parser as ssr_sub_parser
from sub_parser.ss_sub_parser import SSNode
from sub_parser.ssr_sub_parser import SSRNode

server_remote_options = ["tag", "enabled"]
policy_options = ["img-url"]


class RequestParm (Enum):
    FILE_NAME = "filename"
    URL = "url"

    DEFAULT_FILE_NAME = "qx.conf"


class ConfSection(Enum):
    POLICY = "policy"
    SERVER_REMOTE = "server_remote"


def convert(conf_url: str) -> str:
    """ download origin configuration to be converted
    and convert to QuantumultX configuration"""
    conf: Dict[str, Union[list, dict]] = json.loads(
        requests.get(conf_url).text)
    _add_server_remote(conf[ConfSection.POLICY.value],
                       conf[ConfSection.SERVER_REMOTE.value])
    return _serialize(conf)


def _serialize(conf_json: dict) -> str:
    serialized: str = ""
    for section_key in conf_json:
        serialized += "[{0}]\n".format(section_key)
        section = conf_json[section_key]
        try:
            conf_section = ConfSection(section_key)
        except ValueError:
            serialized += "\n".join(line for line in section)
        else:
            if ConfSection(section_key) == ConfSection.POLICY:
                for item_key in section:
                    item = section[item_key]
                    serialized += "{0}={1}".format(item["type"], item_key)
                    serialized += "".join(", {0}".format(p)
                                          for p in item["policies"])
                    serialized += "".join(", {0}={1}".format(
                        option, item[option]) for option in item if option in policy_options)
                    serialized += "\n"
            elif ConfSection(section_key) == ConfSection.SERVER_REMOTE:
                for item in section:
                    serialized += item["url"]
                    serialized += "".join(", {0}={1}".format(
                        option, item[option]) for option in item if option in server_remote_options)
                    serialized += "\n"
        finally:
            serialized += "\n"
    return serialized


def _add_server_remote(policy: Dict[str, Dict[str, Union[str, List[str]]]], remote: List[Dict[str, Union[str, List[str]]]]):
    # download ss_sub_urls & ssr_sub_urls
    ss_sub_urls: List[str] = []
    ssr_sub_urls: List[str] = []
    for subscription in remote:
        sub_type: str = subscription["type"].lower()
        url: str = subscription["url"]
        if sub_type == "ss":
            ss_sub_urls.append(url)
        elif sub_type == "ssr":
            ssr_sub_urls.append(url)
    ss_nodes: Dict[str, List[SSNode]
                   ] = ss_sub_parser.deserialize_urls(ss_sub_urls)
    ssr_nodes: Dict[str, List[SSRNode]
                    ] = ssr_sub_parser.deserialize_urls(ssr_sub_urls)
    # add policies to policy group
    for subscription in remote:
        sub_type: str = subscription["type"].lower()
        url: str = subscription["url"]
        if sub_type == "ss":
            for p in subscription["policies"]:
                policy[p]["policies"].extend(
                    [node.tag for node in ss_nodes[url]])
        elif sub_type == "ssr":
            for p in subscription["policies"]:
                policy[p]["policies"].extend(
                    [node.remarks for node in ssr_nodes[url]])
