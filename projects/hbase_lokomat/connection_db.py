import happybase

def database_connection():
    connection = happybase.Connection('127.0.0.1', 9090)
    connection.open()
    return connection


