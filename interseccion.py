interseccion_lista = []
def interseccion (primer_conjunto,segundo_conjunto):
    for elemento_primer_conjunto in primer_conjunto:
        for elemento_segundo_conjunto in segundo_conjunto:
            if elemento_primer_conjunto == elemento_segundo_conjunto: 
                interseccion_lista.append(elemento_primer_conjunto) 
    return interseccion_lista
