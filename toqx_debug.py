from flask import Flask, request

from main import to_qx

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        #flask.Flask.make_response>`.
        `make_response <http://flask.pocoo.org/docs/1.0/api/
    """
    response = to_qx(request)
    return response


if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0', port=5000)
