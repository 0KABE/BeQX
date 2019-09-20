import conf_parser.ssr as ssr
import conf_parser.ss as ss


def add_server_remote(policy: dict, remote: dict):
    for subscription in remote:
        sub_type: str = subscription["type"].lower()
        if sub_type == "ss":
            sub = ss.RemoteSubscription(subscription["url"])
            for p in subscription["policies"]:
                policy[p]["policies"].extend(sub.nodes)
        elif sub_type == "ssr":
            sub = ssr.RemoteSubscription(subscription["url"])
            for p in subscription["policies"]:
                policy[p]["policies"].extend(sub.nodes)
