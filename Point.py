from math import sqrt, acos, atan, pi

class Point():
    """2D Points"""
    def __init__(self, x, y):
        self.x = round(x, 3)
        self.y = round(y, 3)
        
    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)
        
    def __eq__(self, p):
        return self.x == p.x and self.y == p.y
        
    def __lt__(self, p):
        """El punto con menor coordenada 'y' es menor.
        Si ambos puntos tienen la misma coordenada 'y',
        entonces se considera que el punto de la
        derecha esta un poco mas abajo. O sea, el punto
        de la derecha es menor."""
        if self.y < p.y:
            return True
        elif self.y > p.y:
            return False
        else:
            if self.x > p.x:
                return True
            else:
                return False

    def __gt__(self, p):
        if self.y < p.y:
            return False
        elif self.y > p.y:
            return True
        else:
            if self.x < p.x:
                return True
            else:
                return False
    
