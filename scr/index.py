from flask import Flask, render_template
from scr.views import view_highchart

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def principal():
    return render_template('index.html')


if __name__ == '__main__':
    app.register_blueprint(view_highchart.main,url_prefix='/')
    app.run(host='0.0.0.0', port=5003, debug=True)
