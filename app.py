from flask import Flask, jsonify, abort, render_template, redirect, session

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/<int:code>')
def is_even(code):
    if code % 2 == 0:
        return jsonify(number=code, message="the number is even")
    else:
        return redirect(f"/is_odd/{code}")
        # abort(404)


@app.route('/is_odd/<int:n>')
def is_odd(n):
    if n % 2 != 0:
        return jsonify(number=n, message="the number is odd")
    else:
        abort(404)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("page_not_found.html"), 404


if __name__ == '__main__':
    app.run(debug=True)
