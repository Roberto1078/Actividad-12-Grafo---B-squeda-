import math

def distancia_euclidiana(x_1, y_1 , x_2, y_2) :
    raiz = math.sqrt((x_2 - x_1)**2 + (y_2-y_1)**2)
    return raiz

def recorrido_profundidad(inicio, diccionario) :

    visitados = []
    pila = []
    recorrido = []

    visitados.append(inicio)
    pila.append(inicio)

    while len(pila) > 0 :

        ultimo = pila[-1]
        recorrido.append(ultimo)
      
        lista = list(diccionario[ultimo])
        adyacente = []
        for p in lista :
            adyacente.append(p[0])
        pila.pop()
        for p in adyacente :
            if not p in visitados :
                pila.append(p)
        
        for p in adyacente :
            if not p in visitados :
                visitados.append(p)
    return recorrido

def recorrido_amplitud(inicio, diccionario) :

    visitados = []
    pila = []
    recorrido = []

    visitados.append(inicio)
    pila.append(inicio)

    while len(pila) > 0 :

        ultimo = pila[0]
        recorrido.append(ultimo)
      
        lista = list(diccionario[ultimo])
        adyacente = []
        for p in lista :
            adyacente.append(p[0])
        pila.pop(0)
        for p in adyacente :
            if not p in visitados :
                pila.append(p)
        
        for p in adyacente :
            if not p in visitados :
                visitados.append(p)
    return recorrido