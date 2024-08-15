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

    @staticmethod
    def get_ejemplo_3():
        connection = get_connection_SQLSERVER()
        with connection.cursor() as cursor:
            try:
                query = "select zona_cobranza,forma_de_pago,monto_cobrado from cobranzaxzona"
                cursor.execute(query)
                result = cursor.fetchall()
                return result
            except Exception as e:
                print(f"Error en la consulta {str(e)}")
                return []

    @staticmethod
    def get_ejemplo_4():
        connection = get_connection_SQLSERVER()
        with connection.cursor() as cursor:
            try:
                query = "select month(fecha)as mes, monto from Ventas"
                cursor.execute(query)
                result = cursor.fetchall()
                return result
            except Exception as e:
                print(f"Error en la consulta {str(e)}")
                return []

    @staticmethod
    def get_ejemplo_5():
        connection = get_connection_SQLSERVER()
        with connection.cursor() as cursor:
            try:
                #pivot
                query = "SELECT  country, gold, silver, bronze FROM " \
                        " (select country ,quantities,medals from olympic_medals) As sourceTable" \
                        " PIVOT (SUM(quantities)FOR medals IN([gold],[silver],[bronze]))as PivotTable"
                cursor.execute(query)
                result = cursor.fetchall()
                return result
            except Exception as e:
                print(f"Error en la consulta {str(e)}")
                return []

    @staticmethod
    def get_month_names():
        connection = get_connection_SQLSERVER()
        months = []
        with connection.cursor() as cursor:
            try:
                query = "select DATENAME(MONTH,fecha)as month_name " \
                        "from Ventas group by DATENAME(MONTH,fecha), MONTH(fecha) ORDER BY MONTH(fecha)"
                cursor.execute(query)
                rows = cursor.fetchall()
                for row in rows:
                    months.append(row.month_name)

                return months
                print(months)
            except Exception as e:
                print(f"Error en la consulta {str(e)}")
                return []
