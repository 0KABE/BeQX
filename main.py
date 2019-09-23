import re
from flask import Request, make_response

import qx2qx
import qx2clashr


def to_qx(request: Request):
    url: str = request.args.get(qx2qx.RequestParm.URL.value)
    file_name: str = request.args.get(
        qx2qx.RequestParm.FILE_NAME.value, qx2qx.RequestParm.DEFAULT_FILE_NAME.value)

    response = make_response(qx2qx.convert(url))
    response.headers["Content-Disposition"] = "attachment; filename="+file_name
    return response


def to_clashr(request: Request):
    url: str = request.args.get(qx2clashr.RequestParm.URL.value)
    file_name: str = request.args.get(
        qx2clashr.RequestParm.FILE_NAME.value, qx2clashr.RequestParm.DEFAULT_FILE_NAME.value)

    response = make_response(qx2clashr.convert(url))
    response.headers["Content-Disposition"] = "attachment; filename="+file_name
    return response
