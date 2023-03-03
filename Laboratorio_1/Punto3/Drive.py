from Tree import BTree
import pandas as pd
import os

#==================================================
#Parte del lectura del csv
ruta_archivo = os.path.join("Punto3\Data", "salarios.csv")  #<-- Ingrese aqui el nombre de su archivo 
df = pd.read_csv(ruta_archivo) 
Salarios = []
for i in range(df.shape[0]):
    Salarios.append(int(df["Salario"][i]))
#==================================================

'''
Problema: Hallar una distribucion aproximada de los salarios de cierta muestra de 30 colombianos
solucion: Se usan arboles B los cuales optimizan mejor el uso de las bases de datos y nos ayuda ver 
          de mejro manera una distribiucion de los datos.
          Implementamos un metodo de agregar un nodo y usamos la libreria anytree para imprimir 
          luego podiamos constatar gracias a la visualizacion como se distribuian los datos
'''

btree = BTree(3)
btree.insertMultipleNodes(Salarios)
print("Salario representado en arboles BA")
btree.print_tree()
print("Note que el sub-arbol derecho y el sub-arbol izquierdo al ver cual es mayot nos dice cual es el standar mas comun de salarios en colombia ")

