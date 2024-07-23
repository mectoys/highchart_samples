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


@main.route('/ejemplo3')
def sample3():
    result = model_highchart.get_ejemplo_3()
    data = {}
    # procesar datos
    for row in result:
        zona = row.zona_cobranza
        forma_pago = row.forma_de_pago
        monto = row.monto_cobrado
        if zona not in data:
            data[zona] = {}
        data[zona][forma_pago] = monto
    # prepara las categorias(zonas)
    # eje x grafico
    categories = list(data.keys())
    # preparar los datos de las serie
    series_data = []
    formas_pago = list(set(fp for zona in data.values() for fp in zona.keys()))
    # organizar los datos de la serie
    for forma_pago in formas_pago:
        data_for_forma_pago = [data[zona].get(forma_pago, 0) for zona in categories]
        series_data.append(
            {
                'name': forma_pago,
                'data': data_for_forma_pago
            }
        )
        print(series_data)
    return render_template('ejemplo3.html', categories=categories, series_data=series_data)


@main.route('/ejemplo4')
def sample4():
    result = model_highchart.get_ejemplo_4()
    print(result)
    data = {
        'meses': model_highchart.get_month_names(),
        'montos': [0] * 12  # inicializar con 12 ceros
    }
    for row in result:
        mes = row.mes
        if 1 <= mes <= 12:  # asegurar que este dentro del rango
            monto = float(row.monto)
            data['montos'][mes - 1] += monto
        print(data)
    return render_template('ejemplo4.html', data=data)
