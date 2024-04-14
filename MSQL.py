import mysql.connector

conexion = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Administrador1234",
    database = "tienda",
)
cursor = conexion.cursor()

cursor.execute("SHOW TABLES")


tables = cursor.fetchall()

for table in tables:
    table_name = table[0]
    print(f"contenido de la tabla '{table_name}';")

    cursor.execute(f"SELECT * FROM {table_name}")

    rows = cursor.fetchall()

    for row in rows:
        print(row)
    cursor.close

    conexion.close