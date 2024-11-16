def carga_canciones():
    lista_canciones = []
    with open("biblioteca.txt" , "r") as fichero:
        for linea in fichero:
            try:
                cancion,artista,genero = linea.strip().split(" - ")
                dic = {"cancion":cancion,"artista":artista,"genero":genero} # dentro de este diccionario creo como un "guia" donde se ubicaran los nuevos datos
                lista_canciones.append(dic)
            except ValueError:
                print(f"error")
    for mostrar in lista_canciones:
        print(mostrar)    
    return lista_canciones

def agregar_cancion(cancion , artista , genero):
    with open("biblioteca.txt" , "a") as fichero:
        fichero.write("\n"+cancion.capitalize() +" - "+ artista.capitalize() +" - "+ genero.capitalize())
    

#def agregar_cancion(): #Otra forma de hacerlo pero pasandole un diccionario dentro di dicha funcion
#
#    nueva_cancion = {
#        "cancion": "Yesterday",
#        "artista": "The Beatles",
#        "genero": "Classic"
#    }
#
#    with open("biblioteca.txt", "a") as fichero:
#        fichero.write(f"{nueva_cancion['cancion']} - {nueva_cancion['artista']} - {nueva_cancion['genero']}\n")

def eliminar_canciones(lista_canciones , titulo_cancion):
    lista_canciones = [cancion_dic for cancion_dic in lista_canciones if cancion_dic["cancion"] != titulo_cancion]
    with open("biblioteca.txt", "w") as fichero:
        for cancion in lista_canciones:
            fichero.write(f"{cancion['cancion']} - {cancion['artista']} - {cancion['genero']}\n")
    
    for mostrar in lista_canciones:
        print(mostrar) 
    return lista_canciones

def contar_canciones(lista_canciones):
    num_canciones = len(lista_canciones)
    print(f"hay {num_canciones} canciones")

def buscar_por_artista(lista_canciones , titulo_artista):
    print(f"Canciones de {titulo_artista}: ")
    for cancion in lista_canciones:
        if cancion["artista"] == titulo_artista:
            print(f"{cancion["cancion"]}")

def ordenar_alfabeticamente(lista_canciones):
    canciones_ordenadas = sorted(lista_canciones, key=lambda cancion: cancion["cancion"])  # ¿Se puede usar otra cosa que no sea lambda?
    for cancion in canciones_ordenadas:
        print(cancion["cancion"])

def guardar_canciones(lista_canciones_f , archivo):
    with open(archivo, "w")as fichero:
        for cancion in lista_canciones_f:
            fichero.write(f"{cancion["cancion"]} - {cancion["artista"]}\n")


canciones_todas = carga_canciones()
print("-------------------------------")
nueva_cancion = agregar_cancion("Imagine", "John Lennon", "Classic")

canciones_todas =  eliminar_canciones(canciones_todas , "Purple Haze") # ¿por que si no igualo da problemas con la siguiente metodo?
print("----------------------------------")
contar_canciones(canciones_todas)
print("----------------------------")
buscar_por_artista(canciones_todas , "Eagles")
print("--------------------")
ordenar_alfabeticamente(canciones_todas)

canciones_nuevo_f = [
    {"cancion": "unaCancion", "artista": "unArtista"},
    {"cancion": "da igual", "artista": "algo aleatorio"},
    {"cancion": "otraCancion", "artista": "otroArtista"}
] 

guardar_canciones(canciones_nuevo_f , "otraBiblioteca.txt")

