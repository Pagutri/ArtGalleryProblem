__all__ = ['Dcel', 'Vertex', 'Edge', 'Face']

from Point import Point

class Vertex:
    def __init__(self, punto):
        """'punto' debe ser de la clase 'Point'."""
        self.p = punto
        self.in_edge = None # Incident Edge
        
    def __repr__(self):
        return '(%f, %f)' % (self.p.x, self.p.y)


class Face:
    def __init__(self, outer_component, inner_component):
        """'outer_component' e 'inner_component' deben
        ser de la clase 'Edge'."""
        self.out_edge = outer_component
        self.in_edge = inner_component
        
      
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
        self.edges = []
        self.faces = []
        self.build_dcel(x_list, y_list)
        
    def print_vertices(self):
        for v in self.vertices:
            print(v)
            
    def print_edges(self):
        #for i in range(0, len(self.edges), 2):
        for i in range(len(self.edges)):
            print(self.edges[i].origin, "-->", self.edges[i].next.origin)
        
    def build_dcel(self, x_list, y_list):
        n = len(x_list)
        m = len(y_list)
        if m != n:
            print("Error en build_dcel(): 'y_list' y 'x_list' tienen distinta longitud.")
            #break
            
        # Crear la lista de vértices
        for i in range(n):
            p = Point(x_list[i], y_list[i])
            self.vertices.append(Vertex(p))
        # El último punto en las listas es el mismo que el
        # primero para poder cerrar el polígono al graficar.
        # Aquí no necesitamos que se repitan puntos
        self.vertices.pop()
        n = n - 1
            
        # Crear la lista de aristas
        for i in range(n - 1):
            h1 = Edge(self.vertices[i])
            h2 = Edge(self.vertices[i + 1])
            h1.twin = h2
            h2.twin = h1
            self.edges.append(h1)
            self.edges.append(h2)
            
        h1 = Edge(self.vertices[n - 1])
        h2 = Edge(self.vertices[0])
        h1.twin = h2
        h2.twin = h1
        self.edges.append(h1)
        self.edges.append(h2)
            
        # Se asume que al inicio solo hay dos caras:
        # la del interior del poligono y el exterior,
        # y que las caras se recorren en sentido antihorario
        self.faces.append(Face(self.edges[0], None))
        self.faces.append(Face(None, self.edges[1]))
        
        # Identificar las aristas next y prev
        m = len(self.edges)
        print("n=", n, "m=", m)
        for i in range(m):
            if i%2 == 0: # Aristas interiores a la cara inicial
                self.edges[i].next = self.edges[(i + 2)%m]
                self.edges[i].prev = self.edges[i - 2]
                self.edges[i].in_face = self.faces[0]
            else: # Aristas exteriores a la cara inicial
                self.edges[i].next = self.edges[i - 2]
                self.edges[i].prev = self.edges[(i + 2)%m]
                self.edges[i].in_face = self.faces[1]
            
                   
            
            
            
            
            
            
            
            
            
            
            
