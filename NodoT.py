from Point import Point
from Segment import Segment

class NodoT:
    """Árbol binario para guardar la vecindad de los segmentos
    en la línea de barrido cada vez que se alcanza un punto
    evento. El orden es de izquierda a derecha."""
    def __init__(self, segmento):
        self.key = segmento
        self.left = None
        self.right = None
        
def insertar(nodo, segmento):
    # Crear nuevo nodo
    if nodo is None:
        return NodoT(segmento)

    if segmento < nodo.key:
        nodo.left = insertar(nodo.left, segmento)
    else:
        nodo.right = insertar(nodo.right, segmento)
    return nodo

def inorder(root):
    if root is not None:
        inorder(root.left)
        print("[(", root.key.p1.x, root.key.p1.y, ")(", root.key.p2.x, root.key.p2.y, ")]\n")
        root.key.dibujar()
        inorder(root.right)
        
def nodo_minimo(nodo):
    current = nodo
    
    while current and current.left is not None:
        current = current.left

    return current
    
def borrar_nodo(root, key):
    # base Case
    if root is None:
        return root

    # If the key to be deleted is
    # smaller than the root's key,
    # then it lies in left subtree
    if key < root.key:
        root.left = borrar_nodo(root.left, key)

    # If key is same as root's key,
    # then this is the node
    # to be deleted
    elif key == root.key:

        # Node with only one child
        # or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # Node with two children:
        # Get the inorder successor(smallest
        # in the right subtree)
        temp = nodo_minimo(root.right)

        # Copy the inorder successor's
        # content to this node
        root.key = temp.key

        # Delete the inorder successor
        root.right = borrar_nodo(root.right, temp.key)

    # If the key to be deleted is
    # greater than the root's key,
    # then it lies in right subtree
    else:
        root.right = borrar_nodo(root.right, key)

    return root


def buscar_nodo(raiz, key):
    """Devuelve el nodo que contiene 'key' si lo
    encuentra en el arbol y None si no."""
    if raiz == None:
        return None
    if raiz.key == key:
        return raiz
    if key < raiz.key:
        return buscar_nodo(raiz.left, key)
    else:
        return buscar_nodo(raiz.right, key)


def nodo_maximo(raiz):
    current = raiz
    
    while current and current.right is not None:
        current = current.right

    return current
    
    
def vecino_izquierda(raiz, nodo):
    """Encuentra el vecino de la izquierda
    de 'nodo'."""
    pass
    
    
    
    
    
