from flask import Blueprint, render_template

main = Blueprint('highchart_bp', __name__)


@main.route('/ejemplo1')
def sample1():
    # datos para el gráfico
    data = [5, 10, 20, 25,52]

    return render_template('ejemplo1.html', data=data)
