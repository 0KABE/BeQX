from typing import Dict, List, Union

import sub_parser.ss_sub_parser as ss_sub_parser
import sub_parser.ssr_sub_parser as ssr_sub_parser
from sub_parser.ss_sub_parser import SSNode
from sub_parser.ssr_sub_parser import SSRNode


def add_server_remote(policy: Dict[str, Dict[str, Union[str, List[str]]]], remote: List[Dict[str, Union[str, List[str]]]]):
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

    for subscription in remote:
        sub_type: str = subscription["type"].lower()
        url: str = subscription["url"]
        if sub_type == "ss":
            # sub = ss.RemoteSubscription(subscription["url"])
            for p in subscription["policies"]:
                policy[p]["policies"].extend(
                    [node.tag for node in ss_nodes[url]])
        elif sub_type == "ssr":
            # sub = ssr.RemoteSubscription(subscription["url"])
            for p in subscription["policies"]:
                policy[p]["policies"].extend(
                    [node.remarks for node in ssr_nodes[url]])
