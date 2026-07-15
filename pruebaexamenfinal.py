def  leer_opcion():
    while True:
        try:
            opcion_menu=int(input("ingresa una opcion del menu (1-6) : "))
            if 1 <= opcion_menu <= 6:
                return opcion_menu
            else:
                print("Opción no válida. Por favor, ingresa un número entre 1 y 6.")
        except ValueError:
            print("Error, elige una opcion valida")

def buscar_codigo(codigo):
    if codigo in peliculas:
        return True
    
    return False

def cupos_genero( genero):
    total=0
    for codigo in peliculas:
        if peliculas[codigo][1].lower() ==genero.lower():

            genero= peliculas[codigo][1]
            cupos=cartelera[codigo][1]

            total = total + cupos
    print(f" el total de peliculas del genero {genero}: y los cupos son:  : { total}")

def buscar_codigo(codigo):
    if codigo in peliculas:
        return True
    
    return False

def busqueda_precio(p_min, p_max):
    lista_peliculas =[]

    for codigo in peliculas:
        if peliculas[codigo][0] >=p_min and peliculas[codigo][0] <=p_max and cartelera[codigo][1]>0:

            titulo=peliculas[codigo][0]
            precio=cartelera[codigo][0]
            lista_peliculas.append(titulo +"--"+codigo)
            lista_peliculas.sort()
            if len(lista_peliculas)==0:
                print("no hay peliculas en ese rango de precio")
            else:
                for pelicula in lista_peliculas:
                    print (pelicula)
def actualizar_precio(codigo, nuevo_precio):
    if codigo in cartelera:
        cartelera[codigo][0] = nuevo_precio
        print(f"Precio de la película {codigo} actualizado a {nuevo_precio}")
    else:
        print("Código de película no encontrado")


#validaciones
def validar_codigo(codigo):
    if codigo.strip() !="" and not cartelera:
        return True
    return False

def validar_titulo(titulo):
    if titulo.strip() !="":
        return True
    return False
def validar_genero(genero):
    if genero.strip()!="":
        return True
    return False

def validar_duracion(duracion):
    if duracion >0:
        return True
    return False

def validar_clasificacion(clasificacion):
    if clasificacion.lower() =="A" or clasificacion.lower()=="B" or clasificacion.lower() =="C":
        return True
    return False
def validar_idioma(idioma):
    if idioma.strip() !="":
        return True
    return False
def validar_es_3d( es_3d):
    if es_3d.lower() =="s" or es_3d.lower() =="n":
        return True
    return False
def validar_precio(precio):
    if precio >0:
        return True
    return False
def validar_cupos(cupos):
    if cupos >=0:
        return True
    return False

def agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d,
precio, cupos):
    if codigo in peliculas:
        print("el codigo existe)")
    else:
        if validar_codigo(codigo) and validar_titulo(titulo) and validar_genero(genero) and validar_duracion(duracion) and validar_clasificacion(clasificacion) and validar_idioma(idioma) and validar_es_3d(es_3d) and validar_precio(precio) and validar_cupos(cupos):
            peliculas[codigo] =[titulo, genero, duracion, clasificacion, idioma,es_3d]
            cartelera [codigo]= [precio,cupos]
          
        
            print(f"pelicula agregada correctamente {peliculas}")
def eliminar_pelicula(codigo):
    if buscar_codigo(codigo) in peliculas:
        del peliculas[codigo]
        del cartelera[codigo]
        print (f"pelicula eliminada con exito {codigo}")

    

def menu():

    peliculas = {
        'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
        'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
        'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español',
        False],
        'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
        'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
        'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles',
        False],

    }

    cartelera = {
        'P101': [5990, 40],
        'P102': [7990, 0],
        'P103': [4990, 25],
        'P104': [6990, 12],
        'P105': [8990, 8],
        'P106': [7490, 3],

        }


    
    while True:
        print("========== MENÚ PRINCIPAL ==========")
        print("1. Cupos por género")
        print("2. Búsqueda de películas por rango de precio")
        print("3. Actualizar precio de película")
        print("4. Agregar película")
        print("5. Eliminar película")
        print("6. Salir")
        print("=====================================")

        opcion_menu=leer_opcion()

      
        if opcion_menu ==1:
            genero=input(" ingresa el genero de pelicula que quieres buscar: ").upper()
            cupos_genero(genero)

        elif opcion_menu ==2:
            try:
                p_min =int(input ("ingresa el precio minimo :"))
                p_max=int(input ("ingresa el precio maximo :"))
                resultado= busqueda_precio(p_min,p_max, peliculas,cartelera)
                if resultado :
                    print("peliculas encontradas")
                else:
                    print("no hay peliculas en este rango de precios")
            except ValueError:
                print("error, ingresa un numero valido")

        elif opcion_menu ==3:
            codigo=input ("ingresa el codigo :" ).upper()
            try:
                nuevo_precio =int(input("ingresa el nuevo precio: "))
                actualizar_precio(codigo, nuevo_precio)
            except ValueError:
                print("error: por favor ingresa un precio válido)")
        elif opcion_menu ==4:
            codigo=input("ingresa el codigo: ").upper()
            titulo=input("ingresa el titulo: ")
            genero=input("ingresa el genero: ")
            duracion=int(input("ingresa la duracion: "))
            clasificacion=input("ingresa la clasificacion: ").upper()
            idioma=input("ingresa el idioma: ")
            es_3d=input("es 3D? (s/n): ")
            if es_3d.lower() == "s":
                es_3d = True
            else:
                es_3d = False
            precio=int(input("ingresa el precio: "))
            cupos=int(input("ingresa los cupos: "))
        elif opcion_menu ==5:
            codigo=input("ingresa el codigo de la pelicula a eliminar: ").upper()
            eliminar_pelicula(codigo)
        elif opcion_menu ==6:
            print ("Programa finalizado")
            break




if __name__=="__main__":
    menu()