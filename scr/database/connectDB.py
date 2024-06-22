import os
import pyodbc
from dotenv import load_dotenv

load_dotenv("parameters.env")


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
