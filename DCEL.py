class Vertex:
    def __init__(self, punto):
        """'punto' debe ser de la clase 'Point'."""
        self.p = punto
        self.incident_edges = []
        
        
class HalfEdge:
    def __init__(self, origin_vertex):
        """'origin_vertex' debe ser de la clase 'Vertex'."""
        self.origin = origin_vertex
        self.twin = None
        self.next = None
        self.prev = None
        
        
class Dcel:
    def __init__(self, vertices_input = [], edges_input = []):
        """'vertices_input' contiene elementos de la clase 'Point'.
        'edges_input' contiene elementos de la clase 'Segment'."""
        self.vertices = []
        self.half_edges = []
        
    def build_dcel(self):
        for vertex in self.vertices_input:
            self.vertices.append(Vertex(vertex))
            
        for edge in self.edges_input:
            h1 = HalfEdge(edge.p1)
            h2 = HalfEdge(edge.p2)
            h1.twin = h2
            h2.twin = h1
            self.vertices[edge.p1].incident_edges.apppend(h1)
            self.vertices[edge.p2].incident_edges.apppend(h2)
            self.half_edges.apppend(h2)
            self.half_edges.apppend(h1)
            
        for vertex in self.vertices:
            
                   
            
            
            
            
            
            
            
            
            
            
            
