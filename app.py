import mysql.connector
from dueno import Dueno
from menuDueno import MenuDueno
from menuInvernadero import MenuInvernadero
from menuUsuario import MenuUsuario
from menuPlanta import MenuPlanta
conexion = mysql.connector.connect(user='michel', password='12345', database='invernadero')
cursor = conexion.cursor()

while True:
    print("1) Menu Dueño")
    print("2) Menu Invernadero")
    print("3) Menu Usuario")
    print("4) Menu Planta")
    print("0) Salir")
    op = input()
    
    if op == "1":
        menuD = MenuDueno(conexion, cursor)
    elif op == "2":
        menuI = MenuInvernadero(conexion, cursor)
    elif op == "3":
        menuU = MenuUsuario(conexion, cursor)
    elif op == "4":
        menuP = MenuPlanta(conexion, cursor)
    elif op == "0":
        break
#d = Dueno(conexion, cursor)
#d.crear('michel3', 'davalos boites')
#print(d.recuperar())