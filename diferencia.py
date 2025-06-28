
#AQUI HAY QUE AGREGAR CODIGO PARA LA DIFFERENCIA
### -------- ESTO LO HICIMOS EN CLASE ----- ###
d= [1,2,3,4]
e= [3,4,5,6]
f = []

def diferencia (d,e):
    for i in d:
        for y in e:
            if i != y: 
                f.append(i) 

diferencia(d,e)
print(f)
### -------- FIN DE LO QUE HICIMOS EN CLASE ----- ###