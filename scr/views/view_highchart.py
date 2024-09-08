from flask import Blueprint, render_template, request, jsonify
from scr.models.model_highchart import model_highchart

main = Blueprint('highchart_bp', __name__)


@main.route('/highchart')
def maintenance():
    # Datos para el gráfico
    data = [5, 10, 15, 20, 25]

    # Renderizar la plantilla HTML con los datos
    return render_template('ejemplo1.html', data=data)


@main.route('/velocimetro')
def spedometer():
    # Renderizar la plantilla HTML con los datos
    result = model_highchart.get_ejemplo2()
    # Procesar los datos para la plantilla
    data = {
        'meses': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        'canales': {}
    }
    for row in result:
        mes = row.mes - 1  # Restar 1 para ajustar al índice de la lista
        canal = row.canal_de_venta
        monto = float(row.monto)  # Convertir Decimal a float
        if canal not in data['canales']:
            print([0] * 12)
            data['canales'][canal] = [0] * 12
        data['canales'][canal][mes] += monto
    print(data)
    return render_template('ejemplo2.html', data=data)


@main.route('/ejemplo4')
def sample4():
    result = model_highchart.get_ejemplo4()

    data = {
        'meses': model_highchart.get_month_names(),
        'montos': [0] * 12  # Inicializa con 12 ceros
    }
    for row in result:
        mes = row.mes  # Month is already in 1-12 range
        if 1 <= mes <= 12:  # Ensure the month is within the valid range
            monto = float(row.monto)  # Convertir Decimal a float
            data['montos'][mes - 1] += monto  # Adjust index to be 0-11 for list

    print(data)

    # Renderizar la plantilla HTML con los datos
    return render_template('ejemplo4.html', data=data)


@main.route('/ejemplo3')
def sample3():
    result = model_highchart.get_ejemplo3()
    # Procesar los datos para la plantilla
    data = {}
    for row in result:
        zona = row.zona_cobranza
        forma_pago = row.forma_de_pago
        monto = row.monto_cobrado

        if zona not in data:
            data[zona] = {}
        data[zona][forma_pago] = monto

        # Convertir los datos a un formato adecuado para Highcharts
    categories = list(data.keys())
    series_data = []
    formas_pago = list(set(fp for zona in data.values() for fp in zona.keys()))

    for forma_pago in formas_pago:
        data_for_forma_pago = [data[zona].get(forma_pago, 0) for zona in categories]
        series_data.append({
            'name': forma_pago,
            'data': data_for_forma_pago
        })
    print(series_data)
    # Renderizar la plantilla HTML con los datos
    return render_template('ejemplo3.html', categories=categories, series_data=series_data)


# Función para obtener los datos de las medallas
def obtener_datos_medallas():
    result = model_highchart.get_ejemplo5()
    datas = {
        'paises': [],
        'oro': [],
        'plata': [],
        'bronce': [],
    }

    for row in result:
        datas['paises'].append(row.country)
        datas['oro'].append(row.gold)
        datas ['plata'].append(row.silver)
        datas['bronce'].append(row.bronze)

    # https://en.wikipedia.org/wiki/2024_Summer_Olympics_medal_table
    return datas


@main.route('/ejemplo5')
def sample5():
    datos = obtener_datos_medallas()
    # Renderizar la plantilla HTML con los datos
    print(datos)
    return render_template('ejemplo5.html', datos=datos)


@main.route('/ejemplo6')
def sample6():

    #model_highchart.obtenergeojson()

    # Renderizar la plantilla HTML con los datos
    return render_template('ejemplo6.html')


@main.route('/ejemplo6map', methods=['GET', 'POST'])
def sample6map():
    if request.method == "POST":
        data = request.get_json()
        print(data)
        pais = data.get('paises', None)
        result = model_highchart.get_ejemplo6(pais)
        print(result)
        datas = []
        for row in result:
            datas.append([row['hckey'], row['venta'], row['ciudad']])

        return jsonify(datas)