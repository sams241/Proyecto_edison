class biblioteca:

    #Metodo para definir listas
    def __init__(self):
        self.lista_libros =[["libro",True],["articulo",True],["revista",True],["enciclopedia",True],["periodico",True]]

        #Estructura [id,nombre_libro]
        self.lista_prestamos = []


    def prestamo_estudiante(self,estudiante,nombre_libro):
        for x in self.lista_libros:
            if x[0] == nombre_libro: #Verifica el libro si este dentro de la lista
                if x[1]: #Verifica que el libro este disponible
                    x[1] = False #convierte el estado del libro a falso
                    self.lista_prestamos.append([estudiante[0],nombre_libro]) #añade el id y el libro a la lista de prestamos
                    print(f"{nombre_libro} fue prestado a {estudiante[1]}")
                    return
                else:
                    print("\nLibro en prestamo")
                    return
            print("\nLibro no encontrado en la base de datos")

    def prestamo_docente(self,docente,nombre_libro):
        for x in self.lista_libros:
            if x[0] == nombre_libro: #Verifica el libro si este dentro de la lista
                if x[1]: #Verifica que el libro este disponible
                    x[1] = False #convierte el estado del libro a falso
                    self.lista_prestamos.append([docente[0],nombre_libro]) #añade el id y el libro a la lista de prestamos
                    print(f"{nombre_libro} fue prestado a {docente[1]}")
                    return
                else:
                    print("\nObjeto en prestamo")
                    return
            print("\nObjeto no encontrado en la base de datos")
    
    def devolucion_estudiante(self,estudiante,nombre_libro):

        for x in self.lista_prestamos:
            if x[0] == estudiante[0] and x[1] == nombre_libro: #Compara los parametros dados con los que hay en la lista de prestamos
                for i in self.lista_libros: #Si encuentra coincidencia en ambos...
                    if i[0] == nombre_libro:
                        i[1] = True #Cambia el estado del libro a disponible
                        break
                self.lista_prestamos.remove(x) #Elimina el estudiante y el libro de la lista de prestamos
                print(f"\nObjeto {nombre_libro} devuelto por {estudiante[1]}")
                return
        print(f"\nNo se encontro un prestamo del objeto {nombre_libro} para {estudiante[1]}")

    def devolucion_docente(self,docente,nombre_libro):
        
        for x in self.lista_prestamos:
            if x[0] == docente[0] and x[1] == nombre_libro: #Compara los parametros dados con los que hay en la lista de prestamos
                for i in self.lista_libros: #Si encuentra coincidencia en ambos...
                    if i[0] == nombre_libro:
                        i[1] = True #Cambia el estado del libro a disponible
                        break
                self.lista_prestamos.remove(x) #Elimina al docente y el libro de la lista de prestamos
                print(f"\nObjeto {nombre_libro} devuelto por {docente[1]}")
                return
        print(f"\nNo se encontro un prestamo del objeto {nombre_libro} para {docente[1]}")

    def mostrar_libros(self):
        print("\nLista de objetos bibliotecarios")
        for x in self.lista_libros:
            if x[1]:
                estado = "Disponible"
            else:
                estado ="Prestado"
            print(f"\n{x[0]} {estado}")

    def mostrar_prestamos(self):
        if not self.lista_prestamos:
            print("\nNo hay prestamos activos")
            return
        print("\nPrestamos activos")
        for x in self.lista_prestamos:
            print(f"\nID: {x[0]} Objeto: {x[1]}")