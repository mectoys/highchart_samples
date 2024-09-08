import requests
from scr.database.connectDB import get_connection_SQLSERVER, get_connection_MYSQL


class model_highchart:


    @staticmethod
    def obtenergeojson():

        geolink = ['https://code.highcharts.com/mapdata/countries/mx/mx-all.geo.json', 'https://code.highcharts.com/mapdata/countries/pe/pe-all.geo.json',
                   'https://code.highcharts.com/mapdata/countries/co/co-all.geo.json', 'https://code.highcharts.com/mapdata/countries/cr/cr-all.geo.json',
                   'https://code.highcharts.com/mapdata/countries/ar/ar-all.geo.json','https://code.highcharts.com/mapdata/countries/cl/cl-all.geo.json',
                   'https://code.highcharts.com/mapdata/countries/es/es-all.geo.json']
        index=0
        for lnk in geolink:
            index=index + 1

            # URL del archivo GeoJSON
            url = lnk

            # Descargar el archivo GeoJSON
            response = requests.get(url)
            data = response.json()

            # Recorrer las características del GeoJSON para obtener el hc-key
            print(data['title'])
            pais = data['title']
            for feature in data['features']:
                hc_key = feature['properties'].get('hc-key', 'N/A')  # Obtener el valor de hc-key
                name = feature['properties'].get('name', 'N/A')

                print(f"hc-key: {hc_key}")
                print(f"name: {name}")
                connection = get_connection_MYSQL()

                mi_cursor = connection.cursor()
                queryInsert = "INSERT INTO datageo(idpais, ciudad, hckey )VALUES(%s, %s, %s)"

                values = (index, name, hc_key)

                try:
                    mi_cursor.execute(queryInsert, values)
                except:
                    connection.rollback()

                else:
                    connection.commit()

                finally:
                    connection.close()
    @staticmethod
    def get_ejemplo2():
        connection = get_connection_SQLSERVER()

        with connection.cursor() as cursor:
            try:
                query = "select  month(fecha) as mes,canal_de_venta, SUM(monto)AS monto from ventas" \
                        " GROUP BY fecha,canal_de_venta order by month(fecha)"
                cursor.execute(query)
                result = cursor.fetchall()


                return result
            except Exception as e:
                print(f"Error en la consulta: {str(e)}")
                return []

    @staticmethod
    def get_ejemplo3():

        connection = get_connection_SQLSERVER()
        #zona de cobranza
        with connection.cursor() as cursor:
            try:
                query = "select zona_cobranza,forma_de_pago,monto_cobrado from cobranzaxzona"
                cursor.execute(query)
                result = cursor.fetchall()

                return result
            except Exception as e:
                print(f"Error en la consulta: {str(e)}")
                return []

    @staticmethod
    def get_ejemplo4():
        connection = get_connection_SQLSERVER()
        #fecha con montos
        with connection.cursor() as cursor:
            try:
                query = "select month(fecha)as mes, monto from Ventas"
                cursor.execute(query)
                result = cursor.fetchall()
                return result
            except Exception as e:
                print(f"Error en la consulta: {str(e)}")
                return []


    @staticmethod
    def get_ejemplo5():
        connection = get_connection_SQLSERVER()
        #fecha con montos
        with connection.cursor() as cursor:
            try:
                query = "select country,gold,silver,bronze from " \
                        " (select country,medals,quantities from olympic_medals) as SourceTable " \
                        " PIVOT (SUM(quantities) FOR medals IN ([gold],[silver],[bronze])) as PivotTable;"
                cursor.execute(query)
                result = cursor.fetchall()
                print(result)
                return result
            except Exception as e:
                print(f"Error en la consulta: {str(e)}")
                return []

    @staticmethod
    def get_month_names():
        connection = get_connection_SQLSERVER()
        #listado de meses
        months=[]
        with connection.cursor() as cursor:
            try:
                query = "select  DATENAME(MONTH,fecha)as month_name" \
                        " from  Ventas group by DATENAME(MONTH,fecha),MONTH(fecha) ORDER BY MONTH(fecha)"
                cursor.execute(query)
                rows = cursor.fetchall()
                for row in rows:
                    months.append(row.month_name)

                return months
            except Exception as e:
                print(f"Error en la consulta: {str(e)}")
                return []


    @staticmethod
    def get_ejemplo6(pais):
        connection = get_connection_MYSQL()
        with connection.cursor(dictionary=True) as cursor:
            try:
                print(pais)
                query = """
                    SELECT ciudad, hckey, ROUND(RAND() * (10000 - 500) + 500, 2) AS venta
                    FROM datageo as d
                    INNER JOIN pais p ON p.idpais= d.idpais WHERE p.idpais = %s
                """
                cursor.execute(query, (pais,))
                result = cursor.fetchall()
                return result
            except Exception as e:
                print(f"Error en la consulta: {str(e)}")
                return []