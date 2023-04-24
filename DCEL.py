__all__ = ['Dcel', 'Vertex', 'Edge', 'Face']

class Vertex:
    def __init__(self, punto):
        """'punto' debe ser de la clase 'Point'."""
        self.p = punto
        self.in_edge = None # Incident Edge


class Face:
    def __init__(self, outer_component):
        """'outer_component' debe ser de la clase 'Edge'."""
        self.out_edge = outer_component
        
      
class Edge:
     def __init__(self, origin):
         """'origin' debe ser de la clase 'Vertex'."""
         self.origin = origin
         self.twin = None
         self.in_face = None # Incident Face
         self.next = None
         self.prev = None
         
         
class Dcel:
    def __init__(self, x_list, y_list):
        self.vertices = []
        self.hedges = []
        self.faces = []
        self.build_dcel(x_list, y_list)
        
    def build_dcel(self, x_list, y_list):
        n = len(x_list)
        m = len(y_list)
        if m != n:
            print("Error en build_dcel(): 'y_list' y 'x_list' tienen distinta longitud.")
            #break
            
        # Crear la lista de vértices
        for i in range(n):
            p = Point(x[i], y[i])
            self.vertices.append(Vertex(p))
        # El último punto en las listas es el mismo que el
        # primero para poder cerrar el polígono al graficar.
        # Aquí no necesitamos que se repitan puntos
        self.vertices.pop()
        n = n - 1
            
        # Crear la lista de aristas
        for i in range(n - 1):
            h1 = Edge(vertices[i])
            h2 = Edge(vertices[i + 1])
            h1.twin = h2
            h2.twin = h1
            self.edges.append(h1)
            self.edges.append(h2)
            
        # Identificar las aristas next y prev
        m = len(self.edges)
        for i in range(m):
            if i%2 == 0: # Aristas interiores
                self.edges[i].next = self.edges[i + 2]
                self.edges[i].prev = self.edges[i - 2]
            else: # Aristas exteriores
                self.edges[i].next = self.edges[i - 2]
                self.edges[i].prev = self.edges[i + 2]
                
        # Se asume que al inicio solo hay una cara
        # y que las caras se recorren en sentido antihorario
        self.faces.append(Face(self.edges[0]))
            
            
                   
            
            
            
            
            
            
            
            
            
            
            
