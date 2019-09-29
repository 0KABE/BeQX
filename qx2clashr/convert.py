import json
import re
from enum import Enum
from typing import Dict, List, Union

import requests
import utils
import yaml

from sub_parser import ss as ss_sub_parser
from sub_parser import ssr as ssr_sub_parser
from sub_parser.ss import SSNode
from sub_parser.ssr import SSRNode

built_in_policy = ["direct", "reject", "proxy"]


class RequestParm (Enum):
    FILE_NAME = "filename"
    URL = "url"

    DEFAULT_FILE_NAME = "qx.yml"


class ConfSection(Enum):
    POLICY = "policy"
    SERVER_REMOTE = "server_remote"
    FILTER_REMOTE = "filter_remote"
    FILTER_LOCAL = "filter_local"


def convert(conf_url: str) -> str:
    """ download origin configuration to be converted
    and convert to ClashR configuration"""
    conf: Dict[str, Union[list, dict]] = json.loads(
        requests.get(conf_url).text)

    clash: dict = {}

    proxies: List[Dict[str, str]] = _get_proxies(
        conf[ConfSection.POLICY.value], conf[ConfSection.SERVER_REMOTE.value])
    proxy_groups: List[dict] = _get_proxy_groups(
        conf[ConfSection.POLICY.value])
    rules: List[str] = _get_rules(conf)

    clash["Proxy"] = proxies
    clash["Proxy Group"] = proxy_groups
    clash["Rule"] = rules

    return yaml.dump(clash)


def _get_proxies(policy: Dict[str, dict], server_remote: List[Dict[str, str]]) -> List[Dict[str, str]]:
    proxies: List[Dict[str, str]] = []
    # download ss_sub_urls & ssr_sub_urls
    ss_sub_urls: List[str] = []
    ssr_sub_urls: List[str] = []
    for subscription in server_remote:
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
    proxies.extend(_ss_node_to_dict(node)
                   for ss_node_list in ss_nodes.values()for node in ss_node_list)
    proxies.extend(_ssr_node_to_dict(node)
                   for ssr_node_list in ssr_nodes.values()for node in ssr_node_list)

    # add policies to policy group
    for subscription in server_remote:
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

    return proxies


def _get_proxy_groups(policy: Dict[str, dict]) -> List[dict]:
    return [_get_proxy_group(policy[name], name) for name in policy]


def _get_proxy_group(group: dict, group_name: str) -> dict:
    if group["type"] == "static":
        return {
            "name": group_name,
            "type": "select",
            "proxies": [policy if policy.lower() not in built_in_policy else policy.upper() for policy in group["policies"]],
        }
    elif group["type"] == "available":
        return {
            "name": group_name,
            "type": "fallback",
            "proxies": [policy if policy.lower() not in built_in_policy else policy.upper() for policy in group["policies"]],
            "url": "http://connectivitycheck.gstatic.com/generate_204",
            "interval": "1200"
        }
    elif group["type"] == "round-robin":
        return {
            "name": group_name,
            "type": "load-balance",
            "proxies": [policy if policy.lower() not in built_in_policy else policy.upper() for policy in group["policies"]],
            "url": "http://connectivitycheck.gstatic.com/generate_204",
            "interval": "1200"
        }


def _get_rules(conf: Dict[str, Union[list, dict]]) -> List[str]:
    rule_contents: Dict[str, List[str]] = {item[0]: item[1].splitlines() for item in (utils.download_urls(
        [remote["url"] for remote in conf[ConfSection.FILTER_REMOTE.value]])).items()}
    rules: List[str] = [rl for rl in (_quantumult_x_rule_to_str(rule, remote["force-policy"])
                                      for remote in conf[ConfSection.FILTER_REMOTE.value] for rule in rule_contents[remote["url"]]) if rl is not None]
    rules.extend(_quantumult_x_rule_to_str(rule)
                 for rule in conf[ConfSection.FILTER_LOCAL.value])
    return rules


def _ss_node_to_dict(node: SSNode) -> Dict[str, str]:
    return {
        "name": node.tag,
        "type": "ss",
        "server": node.hostname,
        "port": node.port,
        "password": node.password,
        "cipher": node.method,
        "obfs": node.obfs,
        "obfs-host": node.obfs_host,
    }


def _ssr_node_to_dict(node: SSRNode) -> Dict[str, str]:
    return {
        "name": node.remarks,
        "type": "ssr",
        "server": node.host,
        "port": node.port,
        "password": node.password,
        "cipher": node.method,
        "protocol": node.protocol,
        "protocolparam": node.protoparam,
        "obfs": node.obfs,
        "obfsparam": node.obfsparam
    }


def _quantumult_x_rule_to_str(rule: str, force_policy=None) -> str:
    if re.match("^(#|>|$)", rule.lstrip()):
        return None
    split = rule.split(",", 2)
    if split[0].lower() == "user-agent":
        return None
    if split[0].lower() == "final":
        return "MATCH, "+(split[1].strip() if force_policy == None else force_policy)
    else:
        policy: str = split[2].strip(
        ) if force_policy == None else force_policy
        return "{0},{1},{2}".format(split[0].upper().strip(),
                                    split[1].strip(),
                                    policy if policy.lower() not in built_in_policy else policy.upper())
