from Node import Node

class AVLTree:
	
    def __init__(self) -> None:
        self.root = None

    def Addnode_recursivo(self, node: Node, value: list) -> Node:
        '''
        Esta función nos permite añadir un nodo a un arbol y balancearlo automaticamente
        Input() = 
                    self: objeto Arbol
                    node: objeto Nodo (donde se itera recursivamente)
                    value: Lista fija del nuevo nodo (la primera posicion es la cual nos fijamos para tener el ABB)

        output() = 
                    Node: Objeto nodo (el nuevo nodo que queremos agregar)

        '''
        #Verificamos en caso de que nuestro nodo este vacio para agregarlo 
        if node is None:
            return Node(value)
        #Verificamos los casos de las desigualdades para saber que direccion del arbol ir 
        elif node.value > value[0]:
            #Si nuestro dato es menor eso quiere decir que va en la izquierda
            node.left = self.Addnode_recursivo(node.left, value)
        else:
            #Si nuestro dato es mayor eso quiere decir que va en la derecha
            node.right = self.Addnode_recursivo(node.right, value)

        '''
        Ahora viene lo diferente, pues todo lo anterior es lo mismo que agregar un 
        nodo en un arbol binario comun.
        Pero al ser un arbol AVL tenemos que agregar ciertos factores como la altura 
        y el factor de balance.
        '''
        #Arreglamos la altura de nuestro nodo como uno mas que los subarboles inferiores 
        #Pues recordemos que la altura es la cantidad de ramas que recorremos desde el nodo 
        #hasta una hoja
        node.height = 1 + max(self.Get_height(node.left), self.Get_height(node.right))

        #Calculamos el factor de balance del nodo
        Bf = self.Balanced_factor(node)

        #Identificamos los casos en el que debemos aplicar las roteciones 
        # BF = left.height - right.height

        #Si se cumple este caso eso implica que nuestro desbalance esta por la izquierda
        #Y como nuestro nodo a agregar iria a la izquierda solo hace falta la rotacion simple
        if Bf > 1 and value[0] < node.left.value:
            return self.Simple_right_rotation(node)

        #Si se cumple este caso eso implica que nuestro desbalance esta por la derecha
        #Y como nuestro nodo a agregar iria a la derecha solo hace falta la rotacion simple
        if Bf < -1 and value[0] > node.right.value:
            return self.Simple_left_rotation(node)
        
        #Si se cumple este caso eso implica que nuestro desbalance esta por la izquierda
        #Y como nuestro nodo a agregar iria a la derecha solo hace falta la rotacion doble
        if Bf > 1 and value[0] > node.left.value:
            return self.Double_right_rotation(node)
        
        #Si se cumple este caso eso implica que nuestro desbalance esta por la derecha
        #Y como nuestro nodo a agregar iria a la izquierda solo hace falta la rotacion doble
        if Bf < -1 and value[0] < node.right.value:
            return self.Double_left_rotation(node)

        return node
    
    def Addnode(self, value: list) -> None:
        '''
        Esta función nos permite añadir un nodo a un arbol de una manera mas directa
        Input() = 
                    self: objeto Arbol
                    value: Lista fija del nuevo nodo (la primera posicion es la cual nos fijamos para tener el ABB)

        output() = 
                    None

        '''
        #Verificamos el caso en el que nuestro arbol este vacio
        if self.root is None:
            self.root = Node(value)
        else:
            #De lo contrario ejecutamos nuestra funcion anterior
            self.root = self.Addnode_recursivo(self.root, value)
  
    def addMultipleNodes(self, values: list) -> None:
        '''
        Esta función nos permite añadir multiples nodos a un arbol
        Input() = 
                    self: objeto Arbol
                    values: Listas de valores fijos de los nuevos nodos

        output() = 
                    None

        '''
        #Recorremos nuestra lista de valores
        for node in values:
            #Ejecutamos nuestra funcion anterior en cada iteracion
            self.Addnode(node)    
    
    def Simple_right_rotation(self, node: Node) -> Node:
        '''
        Esta función nos permite balancear un arbol el cual tiene un desbalanceo 
        por la izquierda
        Input() = 
                    self: objeto Arbol
                    node: objeto Nodo (el que sufre el desbalanceo)

        output() = 
                    Node: Objeto nodo (la raiz del nuevo subarbol banaceado)

        '''
        #Reacomodamos la posicion de los nodos de manera que queden balanceados
        child = node.left
        node.left = child.right
        child.right = node
        #Restablecemos nuestra nueva raiz en caso de necesitar
        if node.value == self.root.value:
            self.root = child

        #Al ser un arbol AVL debemos ajustar la altura de los nodos
        node.height = 1 + max(self.Get_height(node.left),self.Get_height(node.right))
        child.height = 1 + max(self.Get_height(child.left),self.Get_height(child.right))

        return child
    
    def Simple_left_rotation(self, node: Node) -> Node:
        '''
        Esta función nos permite balancear un arbol el cual tiene un desbalanceo 
        por la derecha
        Input() = 
                    self: objeto Arbol
                    node: objeto Nodo (el que sufre el desbalanceo)

        output() = 
                    Node: Objeto nodo (la raiz del nuevo subarbol banaceado)

        '''
        #Reacomodamos la posicion de los nodos de manera que queden balanceados
        child = node.right
        node.right = child.left
        child.left = node
        #Restablecemos nuestra nueva raiz en caso de necesitar
        if node.value == self.root.value:
            self.root = child

        #Al ser un arbol AVL debemos ajustar la altura de los nodosm
        node.height = 1 + max(self.Get_height(node.left),self.Get_height(node.right))
        child.height = 1 + max(self.Get_height(child.left),self.Get_height(child.right))

        return child
    
    def Double_right_rotation(self, node: Node) -> Node:
        '''
        Esta función nos permite balancear un arbol el cual tiene un desbalanceo 
        por la izquierda pero con un cruce a su derecha
        Input() = 
                    self: objeto Arbol
                    node: objeto Nodo (el que sufre el desbalanceo)

        output() = 
                    Node: Objeto nodo (la raiz del nuevo subarbol banaceado)

        '''
        #Arreglamos la izquierda del desbalanceo 
        node.left = self.Simple_left_rotation(node.left)
        #Arreglamos la derecha del desbalanceo 
        return self.Simple_right_rotation(node)

    def Double_left_rotation(self, node: Node) -> Node:
        '''
        Esta función nos permite balancear un arbol el cual tiene un desbalanceo 
        por la derecha pero con un cruce a su izquierda
        Input() = 
                    self: objeto Arbol
                    node: objeto Nodo (el que sufre el desbalanceo)

        output() = 
                    Node: Objeto nodo (la raiz del nuevo subarbol banaceado)

        '''
        #Arreglamos la izquierda del desbalanceo 
        node.right = self.Simple_right_rotation(node.right)
        #Arreglamos la derecha del desbalanceo 
        return self.Simple_left_rotation(node)

    def Balanced_factor(self, node: Node) -> int:
        '''
        Esta función nos permite hallar el factor de balance de un nodo
        Input() = 
                    self: objeto Arbol
                    node: objeto nodo al cual queremos calcular su BF

        output() = 
                    Bf: Factor de balance del nodo

        '''
        #Verificamos el caso de no existir el nodo
        if node is None:
            return 0
        #De lo contrario calculamos el BF en base a la formula lef.height - right.height
        return (self.Get_height(node.left) - self.Get_height(node.right))
    
    def Get_height(self, node: Node) -> int:
        '''
        Esta función nos permite hallar la altura de un nodo
        Input() = 
                    self: objeto Arbol
                    node: objeto nodo al cual queremos calcular su altura

        output() = 
                    Height: Altura del nodo (Cantidad de ramas entre el nodo y una hoja)

        '''
        #Verificamos el caso de no existir el nodo
        if node is None:
            return 0 
        #De lo contrario retornamos el parametro altura del nodo
        return node.height

    def Find_family_rucursivo(self, node: Node, value: int, family: list) -> list("Nodo"):
        '''
        Esta funcion nos perimte hallar los antepasados de cierto nodo  
        Input() = 
                    self: objeto Arbol
                    node: objeto Nodo (donde se itera recursivamente)
                    value: Valor fijo del nodo al que le buscamos los antepasados
                    family: Listas donde iran los antepasados del nodo
        Outout() = 
                    family: lista de los antepasados en orden desendente (ultimo papá, penultimo abuelo, ...)
        '''
        #verificamos si el nodo que buscamos es la raiz 
        if self.root.value == value:
            return None
        #hacemos un try-except para almacenar el error en el que el valor que buscamos no este en el arbol
        try:
        #Se verifican los dos casos de desigualdad y se van agregando los antepasados
            if node.value < value:
                family.append(node)
                if node.right.value == value:
                    return family
                else:
                    self.Find_family_rucursivo(node.right, value, family)

            else:

                family.append(node)
                if node.left.value == value:
                    return family
                else:
                    self.Find_family_rucursivo(node.left, value, family)

        except AttributeError:
            return None
        return family
    
    def Find_Grandpa(self, value) -> Node:
        '''
        Esta funcion nos perimte hallar el abuelo del nodo  
        Input() = 
                    self: objeto Arbol
                    value: Valor fijo del nodo al que le buscamos el abuelo
        Outout() = 
                    abuelo: objeto nodo (El nodo padre del nodo)
        '''
        #Tomamos un auxiliar para aligerar el contenido del algoritmo
        aux = self.Find_family_rucursivo(self.root, value, [])
        #Verficamos el caso en el que tenga algun antepasado y que por lo menos tenga abuelo
        if aux is not None and len(aux) > 1:
            return aux[-2].name
        else:
            return None

    def Find_uncle(self, value) -> Node:
        '''
        Esta funcion nos perimte hallar el tio del nodo  
        Input() = 
                    self: objeto Arbol
                    value: Valor fijo del nodo al que le buscamos el tio
        Outout() = 
                    tio: objeto nodo (El nodo padre del nodo)
        '''
        #Tomamos un auxiliar para aligerar el contenido del algoritmo
        aux = self.Find_family_rucursivo(self.root, value, [])
        #Verificamos que tenga antepasado y por lo menos abuelo
        if aux is None or len(aux) < 2:
            return None
        else:
            #Nueva variable para mejor comprension
            Abuelo = aux[-2]
            #Verificamos cual de los hijos del abuelo es el papa del nodo para asi 
            #dar el hijo contrario en caso de existir
            if Abuelo.right != None:
                if Abuelo.right.value == aux[-1].value and Abuelo.left != None:
                    return Abuelo.left.name
            else:
                return None
                
            if Abuelo.left != None:
                if Abuelo.left.value == aux[-1].value and Abuelo.right != None:
                    return Abuelo.right.name
            else:
                return None

    def search(self, node: Node, value: int) -> Node:
        '''
        Esta funcion nos perimte hallar un nodo  
        Input() = 
                    self: objeto Arbol
                    node: objeto nodo (donde se itera recursivamente)
                    value: Valor fijo del nodo que buscamos
        Outout() = 
                    node: objeto nodo (El nodo que buscabamos)
        '''
        #Identificamos que exista o si justo el que iteramos es el que buscamos
        if node is None or node.value == value:
            return node
        #Buscamos por la derecho o izquieda dependiendo de la desigualdad
        if node.value < value:
            return self.search(node.right, value)
        else: 
            return self.search(node.left, value)
    
    def Find_Minimal(self, nodo: Node) -> Node:
        '''
        Esta funcion nos perimte hallar el minimo de un arbol
        Input() = 
                    self: objeto Arbol
                    node: objeto nodo (donde se itera recursivamente)
        Outout() = 
                    node: objeto nodo (El nodo minimo)
        '''
        #Verificamos el caso nulo
        if nodo is None:
            return None
        #Recorremos el arbol solamente por la izquierda pues ahi esta nuestro
        #minimo 
        while(nodo.left != None):
            nodo = nodo.left
        return nodo


    def Delete_node(self, node: Node, value: int) -> Node:
        '''
        Esta funcion nos perimte eliminar un nodo y balancear el resultado
        Input() = 
                    self: objeto Arbol
                    node: objeto nodo (donde se itera recursivamente)
                    value: Valor fijo del nodo que buscamos
        Outout() = 
                    node: objeto nodo (la nueva estructura que remplazara el nodo eliminado )
        '''
        #verificamos el caso nulo
        if node is None:
            return node

        #Verificamos el caso de las desigualdades para encontrar el nodo a eliminar
        if node.value > value:
            node.left = self.Delete_node(node.left, value)
    
        elif node.value < value:
            node.right = self.Delete_node(node.right, value)

        #Verificamos el caso en el que encontramos el nodo
        else:
                     
            #Verificamos el caso en el que tenga solamente un hijo
            if node.left is None:
                temp = node.right
                node = None
                return temp
    
            elif node.right is None:
                temp = node.left
                node = None
                return temp
    
            #En el caso de que sea un nodo con dos hijos
            #Encontramos el minimo del sub-arbol derecho del nodo
            #Para poder balancear 
            temp = self.Find_Minimal(node.right)
            #Y remplazamos
            node.value = temp.value
            node.name = temp.name
            node.right = self.Delete_node(node.right, temp.value)

        #Arreglamos la altura de nuestro nodo como uno mas que los subarboles inferiores 
        #Pues recordemos que la altura es la cantidad de ramas que recorremos desde el nodo 
        #hasta una hoja
        node.height = 1 + max(self.Get_height(node.left),
                            self.Get_height(node.right))
        

        balance = self.Balanced_factor(node)
 
        #Identificamos los casos en el que debemos aplicar las roteciones 
        # BF = left.height - right.height

        #Caso 1 - Left Left
        if balance > 1 and self.Balanced_factor(node.right) >= 0:
            return self.Simple_right_rotation(node)
 
        # Caso 2 - Right Right
        if balance < -1 and self.Balanced_factor(node.left) <= 0:
            return self.Simple_left_rotation(node)
 
        # Caso 3 - Left Right
        if balance > 1 and self.Balanced_factor(node.right) < 0:
            self.Double_right_rotation(node)
 
        # Caso 4 - Right Left
        if balance < -1 and self.Balanced_factor(node.left) > 0:
            self.Double_left_rotation(node)
 
    
        return node

    def Level_nodes(self, node: Node, level: int) -> None:
        '''
        Esta funcion nos perimte Tener los nodos de cierto nivel de un arbol
        Input() = 
                    self: objeto Arbol
                    node: objeto nodo (donde se itera recursivamente)
                    level: Nivel en el cual estamos interesados
        Outout() = 
                    None
        '''
        #Verificamos caso nulo
        if node is None:
            return node
        #Vemos altura por altura
        if level == 1:
            print(node.name, end=' ')
        elif level > 1:
            self.Level_nodes(node.left, level - 1)
            self.Level_nodes(node.right, level - 1)

    def Level_order(self, node: Node) -> None:
        '''
        Esta funcion nos perimte imprimir el arbol en forma trnasversal
        Input() = 
                    self: objeto Arbol
                    node: objeto nodo (donde se itera recursivamente)
        Outout() = 
                    None
        '''
        #Tomamos un uxiliar para aligerar el algoritmo
        aux = self.Get_height(node)
        #Recorremos la altura del arbol e imprimimos los nodos por nivel
        for i in range(1, aux + 1):
            self.Level_nodes(node, i)
            #Lo colocamos asi para evitar escribir None
            print()

    def search_drive(self, node: Node, value: int) -> str:
        '''
        Esta funcion nos perimte hallar un nodo pero ya con su nombre  
        Input() = 
                    self: objeto Arbol
                    node: objeto nodo (donde se itera recursivamente)
                    value: Valor fijo del nodo que buscamos
        Outout() = 
                    name: nombre del nodo a buscar 
        '''
        #Identificamos que exista o si justo el que iteramos es el que buscamos
        if node is None or node.value == value:
            return node.name
        #Buscamos por la derecho o izquieda dependiendo de la desigualdad
        if node.value < value:
            return self.search(node.right, value)
        else: 
            return self.search(node.left, value)

