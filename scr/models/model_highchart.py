from scr.database.connectDB import get_connection_SQLSERVER


class model_highchart:
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
                print(f"Error en la consulta {str(e)}")
                return []
