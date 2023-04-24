def crear_poligono(n, lim):
    """Crea polígono aleatorio de 'n' vértices."""
    delta = 2.0 * np.pi / n
    theta = 0
    lista_x = []
    lista_y = []
    x = random() * lim
    y = random() * lim
    lista_x.append(x)
    lista_y.append(y)
    
    for i in range(n - 1):
        r = random() * lim
        theta += delta
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        lista_x.append(x)
        lista_y.append(y)
        
    return lista_x, lista_y
