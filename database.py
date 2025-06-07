import pyodbc

def get_connection():
    server = 'sqlserverdatafordemocracy.database.windows.net'
    database = 'datafordemocracy'
    username = 'datafordemocracy'
    password = 'AdminHevs01'
    driver = '{ODBC Driver 17 for SQL Server}'
    conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    return pyodbc.connect(conn_str)
