import json
import qx.policy as policy
from enum import Enum
import requests
from flask import Request, make_response


server_remote_options = ["tag", "enabled"]
policy_options = ["img-url"]


def to_qx(request: Request):
    file_name: str = request.args.get("filename", "qx.conf")
    ret: str = ""
    conf: dict = json.loads(requests.get(request.args.get("url")).content.decode())
    policy.add_server_remote(conf["policy"], conf["server_remote"])
    for module_key in conf:
        ret += "\n[" + module_key+"]\n"
        module = conf[module_key]
        if module_key == "policy":
            for item_key in module:
                item = module[item_key]
                ret += str.format("{0} = {1}", item["type"], item_key)
                for p in item["policies"]:
                    ret += str.format(", {0}", p)
                for option in item:
                    if option in policy_options:
                        ret += str.format(", {0}={1}",
                                          option, item[option])
                ret += "\n"
        elif module_key == "server_remote":
            for item in module:
                ret += item["url"]
                for option in item:
                    if option in server_remote_options:
                        ret += str.format(", {0}={1}",
                                          option, item[option])
                ret += "\n"
        else:
            ret += "\n".join(line for line in module)+"\n"
    response = make_response(ret)
    response.headers["Content-Disposition"] = "attachment; filename="+file_name
    return response
