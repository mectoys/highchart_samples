from flask import Blueprint, render_template
from scr.models.model_highchart import model_highchart

main = Blueprint('highchart_bp', __name__)


@main.route('/ejemplo1')
def sample1():
    # datos para el gráfico
    data = [5, 10, 20, 25, 52]

    return render_template('ejemplo1.html', data=data)


@main.route('/ejemplo2')
def sample2():
    result = model_highchart.get_ejemplo2()

    data = {
        'meses': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        'canales': {}
    }

    for row in result:
        mes = row.mes - 1  # restar 1 para ajustar la lista
        canal = row.canal_de_venta
        monto = float(row.monto)
        if canal not in data['canales']:
            data['canales'][canal] = [0] * 12

        data['canales'][canal][mes] += monto
    print(data)
    return render_template('ejemplo2.html', data=data)
