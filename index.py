"""
from flask import Flask, escape, request

app = Flask(__name__)


@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'
"""

"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)
"""


def hello_http(request):
    """ HTTP Cloud Function
    Arg: request (flask.Request)
    Res: arg(s) for flask.make_response
    """
    # name = request.args.get('name', 'World')
    return 'Return from Python function ' + request  # 'Hello, {}!'.format(name)
