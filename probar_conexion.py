import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gestor_tareas"
)

cursor = conexion.cursor()

cursor.execute("SELECT * FROM tareas")

tareas = cursor.fetchall()

for tarea in tareas:
    print(tarea)

cursor.close()
conexion.close()