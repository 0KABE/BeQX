import re
import traceback

from flask import Flask, Request, make_response, request

import qx2clashr
import qx2qx

app = Flask(__name__)


@app.route('/json2qx', methods=['GET', 'POST'])
def to_qx():
    try:
        url: str = request.args.get(qx2qx.RequestParm.URL.value)
        file_name: str = request.args.get(
            qx2qx.RequestParm.FILE_NAME.value, qx2qx.RequestParm.DEFAULT_FILE_NAME.value)

        response = make_response(qx2qx.convert(url))
        response.headers["Content-Disposition"] = "attachment; filename="+file_name
        return response
    except BaseException as e:
        return traceback.format_exc()


@app.route('/json2clashr', methods=['GET', 'POST'])
def to_clashr():
    try:
        url: str = request.args.get(qx2clashr.RequestParm.URL.value)
        file_name: str = request.args.get(
            qx2clashr.RequestParm.FILE_NAME.value, qx2clashr.RequestParm.DEFAULT_FILE_NAME.value)

        response = make_response(qx2clashr.convert(url))
        response.headers["Content-Disposition"] = "attachment; filename="+file_name
        return response
    except BaseException as e:
        return traceback.format_exc()


if __name__ == '__main__':
    app.debug = False
    app.run(host='localhost', port=5000)
