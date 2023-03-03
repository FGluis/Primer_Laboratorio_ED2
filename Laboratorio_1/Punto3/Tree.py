from Node import Node
from anytree import RenderTree

class BTree:
    #Es la clase principal que define el árbol. El constructor toma un parámetro degree que es el grado mínimo del árbol
    def __init__(self, degree: int) -> None:
        self.root = Node(leaf=True)
        self.degree = degree

    #toma un valor value y lo agrega al árbol en la posición correspondiente.
    #Si el nodo en el que se debe insertar ya está lleno, el árbol se divide
    #en dos nodos y el valor se inserta en el nodo adecuado.
    def insert(self, value: int) -> None:
        # Asignar el nodo raíz del árbol B a la variable 'r'
        r = self.root
    
        # Verificar si el número de claves en el nodo raíz 'r' es igual a (2 * self.degree) - 1
        if len(r.keys) == (2 * self.degree) - 1:
            # Si es así, el nodo raíz está lleno, necesitamos un nuevo nodo raíz
            # Crear un nuevo nodo 's' y establecerlo como la nueva raíz del árbol B
            s = Node()
            self.root = s
        
            # Insertar el antiguo nodo raíz 'r' como el primer hijo del nuevo nodo 's'
            s.children.insert(0, r)
        
            # Dividir el antiguo nodo raíz 'r' y mover las claves y los hijos apropiados al nuevo nodo 's'
            self._split_child(s, 0)
        
            # Después de la división, el árbol B está listo para insertar la nueva clave
            self._insert_nonfull(s, value)
        else:
            # Si el número de claves en el nodo raíz 'r' es menor que (2 * self.degree) - 1, 
            # llamar a la función '_insert_nonfull' para insertar la nueva clave 'value' en el nodo 'r' actual
            self._insert_nonfull(r, value)

    #toma una lista de valores y los agrega uno por uno al árbol utilizando la función insert
    def insertMultipleNodes(self, values: list):
        for value in values:
            self.insert(value)
        
    #Se usa internamente para insertar valores en el arbol
    def _insert_nonfull(self, node: Node, value: int) -> None:
        # Obtener el índice de la última clave en el nodo 'node'
        i = len(node.keys) - 1
        
        if node.leaf:
            # Si el nodo 'node' es una hoja, insertar la nueva clave 'value' en el nodo 'node'
            node.keys.append(0)
            while i >= 0 and value < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = value
        else:
            # Si el nodo 'x' no es una hoja, encontrar el hijo apropiado para insertar la nueva clave 'k'
            while i >= 0 and value < node.keys[i]:
                i -= 1
            i += 1
            
            # Verificar si el hijo apropiado está lleno, si es así, dividir el hijo antes de insertar la nueva clave 'k'
            if len(node.children[i].keys) == (2 * self.degree) - 1:
                self._split_child(node, i)
                if value > node.keys[i]:
                    i += 1
                    
            # Después de la división, el hijo apropiado no estará lleno, llamar a la función '_insert_nonfull' 
            # para insertar la nueva clave 'k' en el hijo apropiado
            self._insert_nonfull(node.children[i], value)


    #Se usa internamente para dividir los nodos cuando sea necesario.
    def _split_child(self, node: Node, i: int) -> Node:
        """
        Divide el i-ésimo hijo de x en dos nodos y añade una nueva clave a x.
        x: el nodo padre
        i: el índice del hijo a dividir
        """
        t = self.degree
        y = node.children[i] # y es el nodo a dividir
        z = Node(leaf=y.leaf) # crea un nuevo nodo z, que será el hermano derecho de y

        # Inserta el nuevo nodo z como un nuevo hijo de node, justo después del viejo hijo y
        node.children.insert(i + 1, z)

        # Mueve la clave mediana de y a node
        node.keys.insert(i, y.keys[t - 1])

        # Mueve las claves de la segunda mitad de las claves de y a z
        z.keys = y.keys[t:(2 * t - 1)]
        y.keys = y.keys[0:(t - 1)]

        # Si y no es una hoja, mueve los hijos de la segunda mitad de los hijos de y a z
        if not y.leaf:
            z.children = y.children[t:(2 * t)]
            y.children = y.children[0:(t - 1)]

    # imprime una representación en orden de nivel del árbol. Cada nivel se imprime en una línea separada.
    def print_tree(self):
        for pre, _, node in RenderTree(self.root):
            print("%s%s" % (pre, node.keys))

