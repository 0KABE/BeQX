import json
from enum import Enum

import requests
from flask import Request, make_response

import qx.policy as policy
import qx.constant

server_remote_options = ["tag", "enabled"]
policy_options = ["img-url"]


def to_qx(request: Request):
    file_name: str = request.args.get(
        qx.constant.RequestParm.FILE_NAME.value, qx.constant.RequestParm.DEFAULT_FILE_NAME.value)
    ret: str = ""
    conf: dict = json.loads(requests.get(request.args.get(
        qx.constant.RequestParm.URL.value)).content.decode())
    policy.add_server_remote(
        conf[qx.constant.Conf.POLICY.value], conf[qx.constant.Conf.SERVER_REMOTE.value])
    for module_key in conf:
        ret += "\n[" + module_key+"]\n"
        module = conf[module_key]
        if module_key == qx.constant.Conf.POLICY.value:
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
        elif module_key == qx.constant.Conf.SERVER_REMOTE.value:
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
