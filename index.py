import customtkinter as ctk
import string
import re
import interseccion as interseccion

# Configuración inicial
# Modifica la apariencia de la ventana
ctk.set_appearance_mode("light")
# Setea color por default en la ventana
ctk.set_default_color_theme("green")

# Crear ventana
app = ctk.CTk()
# Crea el título de la ventana
app.title("Formulario Dinámico de Conjuntos")
# Se define el tamaño de la ventana
app.geometry("575x600")
# Opciones de redimensión de la ventana (Se puede modificar)
app.resizable(True, True)

# Colores
verde_lima = "#BFFF00"
verde_oscuro = "#228B22"

# Crea título
titulo = ctk.CTkLabel(
    app,
    text="Ingrese los conjuntos (solo números enteros y comas)",
    font=("Segoe UI", 18, "bold"),
    text_color=verde_oscuro
)
# Se monta en la ventana el título
titulo.pack(pady=20)

# Se crea un contenedor de inputs
contenedor_inputs = ctk.CTkFrame(app, fg_color="transparent")

# Se monta en la ventana el contenedor de inputs
contenedor_inputs.pack(pady=10)

# Lista para guardar inputs inicializada vacia
lista_inputs = []

# Índice de letras (A y B ya usados)
indice_letra = 2

# Validación: solo números y comas, sin espacios
def limpiar(valor):
    # Eliminar espacios y caracteres no válidos
    limpio = ''.join(c for c in valor if c.isdigit() or c == ',')
    # Reemplazar comas múltiples por una sola con una expresión regular
    limpio = re.sub(r',+', ',', limpio)
    return limpio

# Crear input con label y validación
def crear_input(letra):
    # Variable string controlada por la biblioteca
    conjunto = ctk.StringVar()

    # Si hay cambios en los inputs los limpia y elimina datos no validos (Para que no utilicen caracteres equivocados)
    def hay_cambios(*args):
        contenido = conjunto.get()
        limpio = limpiar(contenido)
        if contenido != limpio:
            conjunto.set(limpio)

    # trace_add observa cambios de la variable y ejecuta la función que limpia valores no validos
    conjunto.trace_add("write", hay_cambios)
    # Crea un Label para el imput con la letra que le corresponde
    label = ctk.CTkLabel(
        contenedor_inputs,
        text=f"Conjunto {letra} :",
        font=("Segoe UI", 14),
        text_color="black"
    )
    # Se monta el label en contenedor de inputs.
    label.pack(anchor="w", padx=20)

    #Se crea input nuevo, textvariable es el dato que muestra dentro del input.
    entry = ctk.CTkEntry(
        contenedor_inputs,
        textvariable=conjunto,
        width=300,
        height=40,
        border_width=2,
        corner_radius=10,
    )
    # Se monta el input en el contenedor de inputs
    entry.pack(pady=5)
    # Se agrega a la lista de inputs el nuevo input creado un una tupla con la letra y los datos del conjunto.
    lista_inputs.append((letra, conjunto))
    print(lista_inputs)


# Crear A y B
crear_input("A")
crear_input("B")

# Botón para agregar más inputs TEST
""" def agregar_input():
    global indice_letra
    if indice_letra < 3:
        letra = string.ascii_uppercase[indice_letra]
        crear_input(letra)
        indice_letra += 1
    else:
        print("Se llegó al límite de conjuntos (C)")

boton_agregar = ctk.CTkButton(
    app,
    text="Agregar Conjunto",
    command=agregar_input,
    fg_color="#D0FF00",
    text_color="black",
    hover_color="#A8E600",
    corner_radius=10
)
boton_agregar.pack(pady=15) """

### ---------------- UNION -------------- ###
# Definimos la función
def unir_conjuntos():
    # Creamos un set donde guardar el resultado
    union_de_conjuntos = set()

    # Iteramos la lista de inputs, obteniendo la letra de los conjuntos
    # y los conjuntos para manejarlos
    for letra, conjunto in lista_inputs:

        # Obtenemos el valor real del conjunto con la función .get(), ya que es un objeto de la libreria
        # Lo convertimos a un set para poder unirlos y eliminar repetidos.
        conjunto = set(conjunto.get())

        # Validar que haya conjuntos, si estan vacios corta ejecución
        if len(conjunto) < 1 : 
            print("Los conjuntos estan vacios")
            break  

        # Elimina la coma del conjunto (como los conjuntos estan separados con comas,
        # el set deja una sola y hay que eliminarla para evitar errores) 
        conjunto.remove(",")

        # Une los conjuntos al set union_de_conjuntos, los sets no repiten valores.
        union_de_conjuntos.update(conjunto)

    #Imprime en consola la union de los conjuntos
    print(f"Union de los conjuntos :",sorted(union_de_conjuntos))

    # Ordenamos la union de los conjuntos, los sets estan desordenados.
    union_de_conjuntos_ordenados = sorted(union_de_conjuntos)

    # Ejecuta la funcion para mostrarlos en la pantalla
    mostrar_union_conjuntos(union_de_conjuntos_ordenados)


# Se crea funcion para mostrar la union de los conjuntos
def mostrar_union_conjuntos (union_de_conjuntos):
    #Validación para asegurarnos que tengamos conjuntos
    if len(union_de_conjuntos) > 0 :
        entry_union.configure(text=union_de_conjuntos, text_color="black")
    #Si no tenemos conjuntos mostramos un msj
    else:
        entry_union.configure(text="Los conjuntos estan vacios, agregue valores para continuar", text_color="red")

#Botón unir conjuntos
#Se crea boton para unior los conjuntos, ejecuta la funcion de unir conjuntos
boton_union = ctk.CTkButton(
    app,
    text = "VER UNIÓN",
    command = unir_conjuntos,
    fg_color=verde_lima,
    text_color="black",
    hover_color="#A8E600",
    corner_radius=10
)
# Se monta en la ventana el boton que creamos.
boton_union.pack(pady=5)

# Se crea titulo de la union de los conjuntos
titulo_entry_union = ctk.CTkLabel(
        app,
        text = "Union de los conjuntos : ",
        fg_color= "transparent"
    )
# Se monta en la ventana el titulo de la union de los inputs
titulo_entry_union.pack()

# Se crea label para mostrar la union de los conjuntos
entry_union = ctk.CTkLabel(
        app,
        text = "",
        fg_color= "transparent",
        font=("Segoe UI", 14,'bold')
    )
# Se monta en la ventana la union de los inputs
entry_union.pack(pady=0)

### ---------------- FIN DE UNION -------------- ###


### ---------------- INTERSECCIÓN -------------- ###
#Se crea funcion que se ejecuta al presiona el boton
def interseccion_de_conjuntos():
    #Se inicia varable vacia donde se guardaran los conjuntos
    conjuntos = []
    # Iteramos la lista de inputs y extraemos los conjuntos para ponerlos en la variable conjuntos.
    for letra, conjunto in lista_inputs:
        #Obtenemos el valor y lo guardamos como un set
        conjunto = set(conjunto.get())
        #Si no hay conjuntos paramos la ejecución y mandamos un msj
        if len(conjunto) < 1 : 
            print("Los conjuntos estan vacios")
            break  
        #Si continua la ejecución eliminamos la coma
        conjunto.remove(",")
        # Agregamos cada conjuntos en forma de lista y ordenados a la variable que creamos, 
        conjuntos.append(list(sorted(conjunto)))
    
    # Si conjuntos tiene alementos 
    if len(conjuntos) > 0:
        # Obtenemos el primer conjunto de la variable conjuntos
        primer_conjunto = conjuntos[0]
        # Obtenemos el segundo conjunto de la variable conjuntos
        segundo_conjunto = conjuntos[1]
        # Esto es para poder pasarle los parametros a la función que se importo. 
        
        ## ------- AQUI USAMOS FUNCION DE INTERSECCIÓN IMPORTADA ------ ##        
        interseccion_resuelta = interseccion.interseccion(primer_conjunto, segundo_conjunto)

        # Función para mostrar los resultados en la ventana
        mostrar_interseccion_conjuntos(sorted(set(interseccion_resuelta)))
    else: 
    #Si conjuntos no tiene elementos se ejecuta la función igual para mostrar un msj de ERROR
        mostrar_interseccion_conjuntos(conjuntos)

# Se crea funcion para mostrar la intersección de los conjuntos
def mostrar_interseccion_conjuntos (interseccion_de_conjuntos):
    #Validación para asegurarnos que tengamos conjuntos
    if len(interseccion_de_conjuntos) > 0 :
        entry_interseccion.configure(text=interseccion_de_conjuntos, text_color="black")
    #Si no tenemos conjuntos mostramos un msj
    else:
        entry_interseccion.configure(text="Los conjuntos estan vacios, agregue valores para continuar", text_color="red")

#Botón intersección conjuntos
#Se crea boton para Intersección los conjuntos, ejecuta la funcion de intersección conjuntos
boton_interseccion = ctk.CTkButton(
    app,
    text = "VER INTERSECCIÓN",
    command = interseccion_de_conjuntos,
    fg_color=verde_lima,
    text_color="black",
    hover_color="#A8E600",
    corner_radius=10
)
# Se monta en la ventana el boton que creamos.
boton_interseccion.pack(pady=5)

# Se crea titulo de la interseccion de los conjuntos
titulo_entry_interseccion = ctk.CTkLabel(
        app,
        text = "Interseccion de los conjuntos : ",
        fg_color= "transparent"
    )
# Se monta en la ventana el titulo de la interseccion de los inputs
titulo_entry_interseccion.pack()

# Se crea label para mostrar la interseccion de los conjuntos
entry_interseccion = ctk.CTkLabel(
        app,
        text = "",
        fg_color= "transparent",
        font=("Segoe UI", 14, "bold")
    )
# Se monta en la ventana la interseccion de los inputs
entry_interseccion.pack(pady=0)


### ---------------- FIN DE  INTERSECCIÓN -------------- ###

### ---------------- DIFERENCIA -------------- ###
#Se crea funcion que se ejecuta al presiona el boton
def diferencia_de_conjuntos():
    #Se inicia varable vacia donde se guardaran los conjuntos
    conjuntos = []
    # Iteramos la lista de inputs y extraemos los conjuntos para ponerlos en la variable conjuntos.
    for letra, conjunto in lista_inputs:
        #Obtenemos el valor y lo guardamos como un set
        conjunto = set(conjunto.get())
        #Si no hay conjuntos paramos la ejecución y mandamos un msj
        if len(conjunto) < 1 : 
            print("Los conjuntos estan vacios")
            break  
        #Si continua la ejecución eliminamos la coma del conjunto
        conjunto.remove(",")
        # Agregamos cada conjuntos en forma de lista y ordenados a la variable que creamos, 
        conjuntos.append(list(sorted(conjunto)))
    
    # Si conjuntos tiene alementos 
    if len(conjuntos) > 0:
        # Obtenemos el primer conjunto de la variable conjuntos
        primer_conjunto = conjuntos[0]
        # Obtenemos el segundo conjunto de la variable conjuntos
        segundo_conjunto = conjuntos[1]
        # Esto es para poder pasarle los parametros a la función que se importo. 
        
        ## ------- AQUI USAMOS FUNCION DE DIFERENCIA IMPORTADA ------ ##   

        # FALTA AGREGARLA AQUÍ -----------------------------------------------------     
        diferencia_resuelta = interseccion.interseccion(primer_conjunto, segundo_conjunto)

        ### --------------------------------------------------------------- ###




        # Función para mostrar los resultados en la ventana
        mostrar_diferencia_conjuntos(sorted(set(diferencia_resuelta)))
    else: 
    #Si conjuntos no tiene elementos se ejecuta la función igual para mostrar un msj de ERROR
        mostrar_diferencia_conjuntos(conjuntos)

# Se crea funcion para mostrar la diferencia de los conjuntos
def mostrar_diferencia_conjuntos (diferencia_de_conjuntos):
    #Validación para asegurarnos que tengamos conjuntos
    if len(diferencia_de_conjuntos) > 0 :
        entry_diferencia.configure(text=diferencia_de_conjuntos, text_color="black")
    #Si no tenemos conjuntos mostramos un msj
    else:
        entry_diferencia.configure(text="Los conjuntos estan vacios, agregue valores para continuar", text_color="red")

#Botón diferencia conjuntos
#Se crea boton para diferencia los conjuntos, ejecuta la funcion de diferencia conjuntos
boton_diferencia = ctk.CTkButton(
    app,
    text = "VER DIFERENCIA",
    command = diferencia_de_conjuntos,
    fg_color=verde_lima,
    text_color="black",
    hover_color="#A8E600",
    corner_radius=10
)
# Se monta en la ventana el boton que creamos.
boton_diferencia.pack(pady=5)

# Se crea titulo de la diferencia de los conjuntos
titulo_entry_diferencia = ctk.CTkLabel(
        app,
        text = "Diferencia de los conjuntos : ",
        fg_color= "transparent"
    )
# Se monta en la ventana el titulo de la diferencia de los inputs
titulo_entry_diferencia.pack()

# Se crea label para mostrar la diferencia de los conjuntos
entry_diferencia = ctk.CTkLabel(
        app,
        text = "",
        fg_color= "transparent",        
        font=("Segoe UI", 14, "bold")
    )
# Se monta en la ventana la diferencia de los inputs
entry_diferencia.pack(pady=0)


### ---------------- FIN DE  diferencia -------------- ###

# Ejecutar app
app.mainloop()

#Hacer pseudocodigo
# Falta agregar diferencia
