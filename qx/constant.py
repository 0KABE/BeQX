from enum import Enum


class RequestParm (Enum):
    FILE_NAME = "filename"
    DEFAULT_FILE_NAME = "qx.conf"
    URL = "url"


class Conf(Enum):
    POLICY = "policy"
    SERVER_REMOTE = "server_remote"
