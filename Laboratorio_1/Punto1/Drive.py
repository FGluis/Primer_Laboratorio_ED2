#Importamos librerias importantes para la realizacion del codigo 
from Display import display
from Tree import AVLTree
import pandas as pd
import os

def Id_to_number(id: str) -> int:
    '''
    Esta funcion nos transforma un User_Id en un numero entero
    La logica detras es transformar en entero cada caracter del string ingresado
    Para despues sumarlos en un solo entero (Es claro que puede llegar a repetirse
    algun numero en algun caso especial pero no se tendra encuenta)
    Input():
                ID: es el id del usuario
    Output(): 
                New_Id: Es la conversion numerica del id
    '''
    #Inicializamos nuestra nueva variable
    newid = ""
    #Verificamos que el ID sea un numero
    if id.isnumeric():
        newid = id
    else:
        #Sino recorremos todo nuestro str para identificar caracter por caracter
        #Al identificarlo lo transformamos en entero y lo concatenamos a la nueva variable 
        for i in id:
            if i.isnumeric():
                newid = newid + i
            elif i.isalpha():
                newid = newid + str(ord(i) - 96)
            else:
                newid = newid + str(ord(i))
    Newid = 0
    #Luego recorremos todo nuestra nueva variable y sumamos todos los numeros dentro del str
    #Esto con fin de simpplificar el id 
    for i in newid:
        Newid = int(i) + Newid
    return int(Newid)

def Unique_list(ids: list) -> list:
    '''
    Esta funcion nos elimina los elementos repetidos de una lista
    input():
                ids: lista a la que queremos eliminar repetidos
    output():
                New_Id: Nueva lista 
    '''
    #Inicilizamos nuestra nueva lista
    New_Id = []
    #Recorremos nuestra antigua lista y agregamos los elementos que no esten en nuestra 
    #Nueva lista
    for i in ids:
        if i not in New_Id:
            New_Id.append(i)
    return New_Id


#==================================================
#Parte del lectura del csv
ruta_archivo = os.path.join("Punto1\Data", "User_track_data.csv")  #<-- Ingrese aqui el nombre de su archivo 
df = pd.read_csv(ruta_archivo) 
Ids = []
Names = []
for i in range(df.shape[0]):
    Ids.append(Id_to_number(df["User_ID"][i]))
    Names.append(df["User_name"][i])
#==================================================


#==================================================
#Parte en la que eliminamos los elementos repetidos y creamos nuestra lista
Id = Unique_list(Ids)
Name = Unique_list(Names)
values = []
for i in range(len(Id)):
    values.append([Id[i],Name[i]])
#==================================================


#==================================================
#Creamos Nuestro Arbol y lo imprimimos 
tree = AVLTree()
tree.addMultipleNodes(values)
display(tree.root)
#==================================================

'''
Demostracion de las funciones de los enunciados
Ojo debes acomodar las funciones segun los nuevos ids 
'''
print(" ")
print("Funciones varias")
print(f'El tio de {tree.search(tree.root, 132).name} es {tree.Find_uncle(132)}')
print(f'El abuelo de {tree.search(tree.root, 133).name} es {tree.Find_Grandpa(133)}')
print(f'La altura del nodo {tree.root.name} es {tree.Get_height(tree.root)}')
print(f'El nodo con la id {45} es {tree.search(tree.root, 45).name}')
print(f'Eliminamos a {tree.search(tree.root, 45).name} y {tree.search(tree.root, 105).name}')
tree.Delete_node(tree.root, 105)
tree.Delete_node(tree.root, 45)
print(" ")
print("Arbol luego de eliminar ")
display(tree.root)
print(" ")
print("Impresion por nivel: ")
tree.Level_order(tree.root)