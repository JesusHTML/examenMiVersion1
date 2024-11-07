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

def insertar_canciones(lista_canciones):
    with open("biblioteca.txt" , "a") as fichero:
        cancion = input("Inserta una cancion: ")
        artista = input("ahora el artista: ")
        genero = input("por ultimo el genero: ")
        fichero.write("\n"+cancion.capitalize() +" - "+ artista.capitalize() +" - "+ genero.capitalize())
    return lista_canciones

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
    cancion_fuera = {cancion:"Purple Haze",artista:"Jimi Hendrix",genero:"classic"}
    
    lista_canciones = [cancion_dic for cancion_dic in lista_canciones != cancion_fuera]
    with open("biblioteca.txt", "w") as fichero:
        fichero.write(lista_canciones)

    return lista_canciones
        

def guardar_canciones():
    print("")


carga_canciones()

#insertar_canciones()


eliminar_canciones()

