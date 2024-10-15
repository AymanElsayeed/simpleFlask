import argparse
import os
import sys
from flask import Flask, jsonify, abort, render_template, redirect, session, request
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'file': {
        'class': 'logging.FileHandler',
        'filename': 'errors.log',
        'formatter': 'default',
        'level': 'DEBUG'
    }},
    'root': {
        'level': 'DEBUG',
        'handlers': ['file']
    }
})

from src.config import FactoryConfigClass

app = Flask(__name__)
app.secret_key = 'the random string'


@app.route('/')
def hello_world():
    return render_template('home.html', numbers=session.keys())
    # return 'Hello World!'


@app.route('/<int:code>')
def is_even(code):
    if code % 2 == 0:
        session[str(code)] = True
        app.logger.info(f"{code} is even number")
        return jsonify(number=code, message="the number is even")
    else:
        return redirect(f"/is_odd/{code}")
        # abort(404)


@app.route('/is_odd/<int:n>')
def is_odd(n):
    if n % 2 != 0:
        app.logger.info(f"{n} is odd number")
        session[str(n)] = True
        return jsonify(number=n, message="the number is odd")
    else:
        abort(404)


@app.route('/is_prime', methods=["POST"])
def is_prime():
    number = request.args.get("number")
    if number is None:
        number = request.get_json()['number']
    for i in range(2, number):
        if number % i == 0:
            return jsonify(data=i, message=f"number {number} is not prime")
    return jsonify(data=i, message=f"number {number} is prime")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("page_not_found.html"), 404


if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description="write file")
    # # parser.add_argument("-hp", "--host", help="host ip", type=str, default="0.0.0.0")
    # parser.add_argument("-hp", "--host", help="host ip", type=str, default="0.0.0.0")
    # parser.add_argument("-p", "--port", help="port", type=int, default="30331")
    # parser.add_argument("-d", "--debug", help="debug", type=bool, default=True)
    # parser.add_argument("-env", "--environment", help="environment name", type=str, default="local")

    # args = parser.parse_args()
    # run_env_config = FactoryConfigClass(env=args.environment)
    #app.config.from_object(run_env_config.config)

    # globals().update(run_env_config.config.__dict__)
    env = os.getenv("ENV", "local")
    run_env_config = FactoryConfigClass(env=env)
    # app.config.from_object(run_env_config.config)
    port = os.getenv("FLASK_EXT_PORT", 30331)
    host = os.getenv("FLASK_EXT_HOST", "0.0.0.0")


    print(f"the ENV is {env}", file=sys.stderr)
    print(f"the port is {run_env_config.config.FLASK_EXT_PORT}", file=sys.stderr)
    print(f"the host is {run_env_config.config.HOST}", file=sys.stderr)

    app.run(debug=True,
            port=port,
            host=host
            )
