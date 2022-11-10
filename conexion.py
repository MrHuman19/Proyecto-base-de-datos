import psycopg2
try:
    connection=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='123456789',
        database='PROYECTO'
    )
    print("CONEXION EXITOSA")
    cursor=connection.cursor()
    cursor.execute("SELECT version()")
    row=cursor.fetchone()
    print(row)
    cursor.execute("SELECT * FROM Delitos_sexuales_Polic_a_Nacional")
    row=cursor.fetchall()
    for row in row:
        print(row)
    cursor.execute("SELECT * FROM arma_medio")
    row=cursor.fetchall()
    for row in row:
        print(row)
    cursor.execute("SELECT * FROM delito")
    row=cursor.fetchall()
    for row in row:
        print(row)
    cursor.execute("SELECT * FROM departamento")
    row=cursor.fetchall()
    for row in row:
        print(row)
    cursor.execute("SELECT * FROM genero")
    row=cursor.fetchall()
    for row in row:
        print(row)
    cursor.execute("SELECT * FROM grupo_etario")
    row=cursor.fetchall()
    for row in row:
        print(row)
    cursor.execute("SELECT * FROM municipio")
    row=cursor.fetchall()
    for row in row:
        print(row)            
except Exception as ex:
    print(ex)