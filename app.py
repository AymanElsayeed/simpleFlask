import argparse

from flask import Flask, jsonify, abort, render_template, redirect, session

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
        return jsonify(number=code, message="the number is even")
    else:
        return redirect(f"/is_odd/{code}")
        # abort(404)


@app.route('/is_odd/<int:n>')
def is_odd(n):
    if n % 2 != 0:
        session[str(n)] = True
        return jsonify(number=n, message="the number is odd")
    else:
        abort(404)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("page_not_found.html"), 404


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="write file")
    parser.add_argument("-hp", "--host", help="host ip", type=str, default="127.0.0.1")
    parser.add_argument("-p", "--port", help="port", type=int, default="5000")
    parser.add_argument("-d", "--debug", help="debug", type=bool, default=True)
    parser.add_argument("-env", "--environment", help="environment name", type=str, default="local")

    args = parser.parse_args()

    run_env_config = FactoryConfigClass(env=args.environment)
    globals().update(run_env_config.config.__dict__)
    # app.run(debug=True)
    app.run(debug=args.debug, host=args.host, port=args.port)