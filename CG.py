from flask.ext.bootstrap import Bootstrap
from flask import Flask, render_template

app = Flask(__name__, static_url_path='')
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return app.send_static_file("index.html")


@app.route('/user/<name>')
def hello_name(name):
    return render_template('user.html', name=name)


if __name__ == '__main__':
    app.run()
