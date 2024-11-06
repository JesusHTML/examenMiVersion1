 # Esta lista sera una lista de diccionarios

def carga_canciones():
    lista_canciones = []
    with open("biblioteca.txt" , "r") as fichero:
        for linea in fichero:
            cancion,artista,genero = linea.strip().split(" - ")
            dic = {cancion:"cancion",artista:"artista",genero:"genero"} # dentro de este diccionario creo como un "guia" donde se ubicaran los nuevos datos
            lista_canciones.append(dic)
    #for segmento in lista_canciones:
    #   for barra in segmento:
    #        print(barra)
    for mostrar in lista_canciones:
        print(mostrar)    
    return lista_canciones

def insertar_canciones():
    with open("biblioteca.txt" , "a") as fichero:
        cancion = input("Inserta una cancion: ")
        artista = input("ahora el artista: ")
        genero = input("por ultimo el genero: ")
        fichero.write(cancion.capitalize() +" - "+ artista.capitalize() +" - "+ genero.capitalize()+"\n")

#def insertar_canciones2():
#    with open("blibioteca.txt", "a") as fichero: 
#            cancion,artista,genero = .strip().split(" - ")
#            dic = {cancion:"prueba",artista:"probando",genero:"pruebaprobando"}
#            fichero.write(dic)

#def insertar_caciones3():
#    dic = {}
#    if cancion in dic:
#        print("Esta cancion ya esta")
#    else :
#        lista_canciones[dic] = cancion,artista,genero
#        print(""+ dic + "")   

def eliminar_canciones(lista_canciones , cancion,artista,genero):
    print("")
        

def guardar_canciones():
    print("")


carga_canciones()

insertar_canciones()