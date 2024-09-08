import os
import pyodbc
import mysql.connector
from dotenv import load_dotenv

load_dotenv("parameters.env")


def get_connection_MYSQL():
    print(os.getenv('MY_SQL_HOST'))
    try:
        return mysql.connector.connect(

            host=os.getenv('MY_SQL_HOST'),
            user=os.getenv('MY_SQL_USER'),
            password=os.getenv('MY_SQL_PASSWORD'),
            database=os.getenv('MY_SQL_DATABASE')
        )

    except mysql.connector.Error as err:
        raise err




def get_connection_SQLSERVER():
    connection_string = (
        f"DRIVER={os.getenv('SQL_SERVER_DRIVER')};"
        f"SERVER={os.getenv('SQL_SERVER_SERVER')};"
        f"DATABASE={os.getenv('SQL_SERVER_DATABASE')};"
        f"UID={os.getenv('SQL_SERVER_UID')};"
        f"PWD={os.getenv('SQL_SERVER_PWD')}"
    )
    try:
        connection=pyodbc.connect(connection_string)
        return connection
    except pyodbc.Error as ex:
        print(f"Error de conexion: {ex}")
        raise
