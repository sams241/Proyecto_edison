class persona:

    #Metodo constructor / Definir atributos que usará la clase persona
    def __init__(self,id="",nombre="",telefono="",correo="",direccion=""): #Se agregan valores vacios a las variables para no tener que pasar datos al momento de instanciar
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion

    #Metodo para agregar persona
    def agregar_persona(self):
        lista_personas = []
        Columnas = ["Id","Nombre","Telefono","Correo","Dirección"]
        print("-" * 40)
        print("Agrega persona")
        print("-" * 40)

        for x in Columnas:
            Dato = input(f"\nPor favor, Ingrese {x} de la persona: ")
            while not Dato:
                Dato = input(f"\nEl {x} no puede estar vacio, por favor ingresa un dato: ")
            lista_personas.append(Dato)
        print("\nPersona agregada con exito")
        return lista_personas #Devuelve los datos en una lista
    
#Clase estudiante, Subclase de la clase persona
class Estudiante(persona):

    #Metodo para heredar atributos y metodos de clase padre(persona)
    def __init__(self, id="", nombre="", telefono="", correo="", direccion=""):
        super().__init__(id, nombre, telefono, correo, direccion)
        self.lista_estudiantes = [] #Lista para almacenar estudiantes(Cada persona es guardada como una lista, esta lista coniene listas anidadas)
   
    #Metodo para agregar estudiante
    def agregar_estudiante(self):
        datos_estudiante = self.agregar_persona() #Llamada a metodo heredado(persona)
        self.lista_estudiantes.append(datos_estudiante) #Agregar registro en lista de estudiantes

    def modificar_datos_estudiante(self):
        if not self.lista_estudiantes: #Si no hay nada en la lista de estudiantes, se muestra lo siguiente:
            print("\nNo hay registros de estudiantes aun, debes agregar uno primero")
            return
        
        print("")
        print("-"*40)
        print(f"Actualmente tiene: {len(self.lista_estudiantes)} estudiantes") #muestra al cantidad de registros
        print("-"*40)
        print("")

        valor = 0 #variable para indicar el numero del registro
        for i in self.lista_estudiantes:
            valor = valor+1
            print(f"Registro: {valor} ID: {i[0]} Nombre: {i[1]} Telefono: {i[2]} Correo: {i[3]} direccion: {i[4]}")

        while True:
            cambio_registro = input("\nPor favor, ingrese el numero del registro que desea modificar: ")

            #Verifica que se ingrese algun dato
            if cambio_registro == "":
                print("\n Debes ingresar una opción.")
                continue

            #Valida que sea un numero entero
            try:
                cambio_registro = int(cambio_registro)-1
            except ValueError:
                print("")
                print("-"*40)
                print("Ingrese un número válido.")
                print("-"*40)
                continue
            
            #Verifica que el numero este entre el rango de registros
            if cambio_registro <= -1 or cambio_registro+1 > len(self.lista_estudiantes):
                print("")
                print("-"*40)
                print(f"Ingrese un número entre 1 y {len(self.lista_estudiantes)}.")
                print("-"*40)
                continue

            print(f"\nVas a modificar los datos del usuario: {self.lista_estudiantes[cambio_registro][1]}")
            
            
            #Solicitud de nuevos datos / verificador de ingreso de datos
            Nuevo_id = input("\nIngresa el nuevo id: ")
            while not Nuevo_id:
                 Nuevo_id = input("\nDebes ingresar un id: ")

            nuevo_nombre = input("\nIngresa el nuevo nombre: ")
            while not nuevo_nombre:
                nuevo_nombre = input("\nDebes ingresar un nombre: ")

            nuevo_telefono = input("\nIngresa el nuevo telefono: ")
            while not nuevo_telefono:
                nuevo_telefono = input("\nDebes ingresar un telefono")

            nuevo_direccion = input("\nIngresa la nueva direccion: ")
            while not nuevo_direccion:
                nuevo_direccion = input("\nDebes ingresar una direccion: ")

            nuevo_correo = input("\nIngresa el nuevo correo: ")
            while not nuevo_correo:
                nuevo_correo = input("\nDebes ingresar un correo: ")
            
            #Cambio de datos
            self.lista_estudiantes[cambio_registro][0]= Nuevo_id
            self.lista_estudiantes[cambio_registro][1]= nuevo_nombre
            self.lista_estudiantes[cambio_registro][2]= nuevo_telefono
            self.lista_estudiantes[cambio_registro][3]= nuevo_direccion
            self.lista_estudiantes[cambio_registro][4]= nuevo_correo

            print("")
            print("-"*40)
            print("Datos actulizados con exito :)")
            print("-"*40)
            break
    
    #Metodo para eliminar un registro de la lista de estudiantes
    def eliminar_estudiantes(self):
        if not self.lista_estudiantes: #Si no hay nada en la lista de estudiantes, se muestra lo siguiente:
            print("\nNo hay registros de estudiantes aun, debes agregar uno primero")
            return
        
        print("")
        print("-"*40)
        print(f"Actualmente tiene: {len(self.lista_estudiantes)} estudiantes") #muestra al cantidad de registros
        print("-"*40)
        print("")

        valor = 0 #variable para indicar el numero del registro
        for i in self.lista_estudiantes:
            valor = valor+1
            print(f"Registro: {valor} ID: {i[0]} Nombre: {i[1]} Telefono: {i[2]} Correo: {i[3]} direccion: {i[4]}")

        while True:
            eliminador = input("\nPor favor, ingrese el numero del registro que desea eliminar: ")

        #Verifica que se ingrese algun dato
            if eliminador == "":
                print("\n Debes ingresar una opción.")
                continue

            #Valida que sea un numero entero
            try:
                eliminador = int(eliminador)-1
            except ValueError:
                print("")
                print("-"*40)
                print("Ingrese un número válido.")
                print("-"*40)
                continue
            
            #Verifica que el numero este entre el rango de registros
            if eliminador <= -1 or eliminador+1 > len(self.lista_estudiantes):
                print("")
                print("-"*40)
                print(f"Ingrese un número entre 1 y {len(self.lista_estudiantes)}.")
                print("-"*40)
                continue
            
            print(f"\nVas a eliminar los datos del usuario: {self.lista_estudiantes[eliminador][1]}")

            del self.lista_estudiantes[eliminador] #Eliminar lista de datos del estudiante elegido

            print("")
            print("-"*40)
            print("Datos eliminados con exito :)")
            print("-"*40)
            break

    #Retornar la lista estudiantes
    def obtener_lista_estudiantes(self):
        return self.lista_estudiantes
    
    #Metodo para mostrar los estudiantes
    def mostrar_estudiantes(self):
        if not self.lista_estudiantes: #Si no hay nada en la lista de estudiantes, se muestra lo siguiente:
            print("\nNo hay registros de estudiantes aun, debes agregar uno primero")
            return
        
        print(f"\nActualmente tiene: {len(self.lista_estudiantes)} estudiantes") #muestra al cantidad de registros

        #Imprimir los datos de cada estudiante
        valor = 0
        for i in self.lista_estudiantes:
            valor = valor+1
            print(f"Registro: {valor} ID: {i[0]} Nombre: {i[1]} Telefono: {i[2]} Correo: {i[3]} direccion: {i[4]}")

    def buscar_estudiante(self,id_estudiante):
        for x in self.lista_estudiantes:
            if x[0] == id_estudiante:
                return x
        return None

class docente(persona):

    def __init__(self, id="", nombre="", telefono="", correo="", direccion=""):
        super().__init__(id, nombre, telefono, correo, direccion)
        self.lista_docentes = []

    #Metodo para agregar docente
    def agregar_docente(self):
        datos_docente = self.agregar_persona() #Llamada a metodo heredado(persona)
        self.lista_docentes.append(datos_docente) #Agregar registro en lista de docentes

    #Retornar la lista docente
    def obtener_lista_docentes(self):
        return self.lista_docentes
    
    #Metodo para mostrar los docente
    def mostrar_docentes(self):
        if not self.lista_docentes: #Si no hay nada en la lista de docentes, se muestra lo siguiente:
            print("\nNo hay registros de docentes aun, debes agregar uno primero")
            return
        
        #Imprimir los datos de cada estudiante
        for i in self.lista_docentes:
            print(f"ID: {i[0]} Nombre: {i[1]} Telefono: {i[2]} Correo: {i[3]} direccion: {i[4]}")

    #Metodo para eliminar un registro de la lista de docentes
    def eliminar_docentes(self):
        if not self.lista_docentes: #Si no hay nada en la lista de docentes, se muestra lo siguiente:
            print("\nNo hay registros de estudiantes aun, debes agregar uno primero")
            return
        
        print("")
        print("-"*40)
        print(f"Actualmente tiene: {len(self.lista_docentes)} docentes") #muestra al cantidad de registros
        print("-"*40)
        print("")

        valor = 0 #variable para indicar el numero del registro
        for i in self.lista_docentes:
            valor = valor+1
            print(f"Registro: {valor} ID: {i[0]} Nombre: {i[1]} Telefono: {i[2]} Correo: {i[3]} direccion: {i[4]}")

        while True:
            eliminador = input("\nPor favor, ingrese el numero del registro que desea eliminar: ")

        #Verifica que se ingrese algun dato
            if eliminador == "":
                print("\n Debes ingresar una opción.")
                continue

            #Valida que sea un numero entero
            try:
                eliminador = int(eliminador)-1
            except ValueError:
                print("")
                print("-"*40)
                print("Ingrese un número válido.")
                print("-"*40)
                continue
            
            #Verifica que el numero este entre el rango de registros
            if eliminador <= -1 or eliminador+1 > len(self.lista_docentes):
                print("")
                print("-"*40)
                print(f"Ingrese un número entre 1 y {len(self.lista_docentes)}.")
                print("-"*40)
                continue
            
            print(f"\nVas a eliminar los datos del usuario: {self.lista_docentes[eliminador][1]}")

            del self.lista_docentes[eliminador] #Eliminar lista de datos del docente elegido

            print("")
            print("-"*40)
            print("Datos eliminados con exito :)")
            print("-"*40)
            break

    def modificar_datos_docente(self):
        if not self.lista_docentes: #Si no hay nada en la lista de docentes, se muestra lo siguiente:
            print("\nNo hay registros de estudiantes aun, debes agregar uno primero")
            return
        
        print("")
        print("-"*40)
        print(f"Actualmente tiene: {len(self.lista_docentes)} docentes") #muestra al cantidad de registros
        print("-"*40)
        print("")

        valor = 0 #variable para indicar el numero del registro
        for i in self.lista_docentes:
            valor = valor+1
            print(f"Registro: {valor} ID: {i[0]} Nombre: {i[1]} Telefono: {i[2]} Correo: {i[3]} direccion: {i[4]}")

        while True:
            cambio_registro = input("\nPor favor, ingrese el numero del registro que desea modificar: ")

            #Verifica que se ingrese algun dato
            if cambio_registro == "":
                print("\n Debes ingresar una opción.")
                continue

            #Valida que sea un numero entero
            try:
                cambio_registro = int(cambio_registro)-1
            except ValueError:
                print("")
                print("-"*40)
                print("Ingrese un número válido.")
                print("-"*40)
                continue
            
            #Verifica que el numero este entre el rango de registros
            if cambio_registro <= -1 or cambio_registro+1 > len(self.lista_docentes):
                print("")
                print("-"*40)
                print(f"Ingrese un número entre 1 y {len(self.lista_docentes)}.")
                print("-"*40)
                continue

            print(f"\nVas a modificar los datos del usuario: {self.lista_docentes[cambio_registro][1]}")
            
            #Solicitud de nuevos datos / verificador de ingreso de datos
            Nuevo_id = input("\nIngresa el nuevo id: ")
            while not Nuevo_id:
                 Nuevo_id = input("\nDebes ingresar un id: ")

            nuevo_nombre = input("\nIngresa el nuevo nombre: ")
            while not nuevo_nombre:
                nuevo_nombre = input("\nDebes ingresar un nombre: ")

            nuevo_telefono = input("\nIngresa el nuevo telefono: ")
            while not nuevo_telefono:
                nuevo_telefono = input("\nDebes ingresar un telefono")

            nuevo_direccion = input("\nIngresa la nueva direccion: ")
            while not nuevo_direccion:
                nuevo_direccion = input("\nDebes ingresar una direccion: ")

            nuevo_correo = input("\nIngresa el nuevo correo: ")
            while not nuevo_correo:
                nuevo_correo = input("\nDebes ingresar un correo: ")
            
            #Cambio de datos
            self.lista_docentes[cambio_registro][0]= Nuevo_id
            self.lista_docentes[cambio_registro][1]= nuevo_nombre
            self.lista_docentes[cambio_registro][2]= nuevo_telefono
            self.lista_docentes[cambio_registro][3]= nuevo_direccion
            self.lista_docentes[cambio_registro][4]= nuevo_correo

            print("")
            print("-"*40)
            print("Datos actulizados con exito :)")
            print("-"*40)
            break

    def buscar_docente(self,id_docete):
        for x in self.lista_docentes:
            if x[0] == id_docente:
                return x
        return None

#Clase actividades
class actividad:

    #Definicion de listas
    def __init__(self):
        self.lista_estudiantes = []
        self.lista_docentes = []
        self.lista_actividades = [["musica",[]],["deporte",[]],["danzas",[]]] #lista predefinida de actividades

    #Recibir lista de estudiantes
    def recibir_estdiantes(self,lista_estudiantes):
        self.lista_estudiantes = lista_estudiantes

    #recibir lista de docentes
    def recibir_docentes(self,lista_docentes):
        self.lista_docentes = lista_docentes

    #Metodo para agregar nuevas actividades
    def agregar_nuevas_actividades(self,nombre_actividad):
        for a in self.lista_actividades:
            if a[0] == nombre_actividad:
                print(f"\nLa actividad {nombre_actividad} ya existe")
                return
        self.lista_actividades.append([nombre_actividad,[]])
        print(f"\nLa actividad {nombre_actividad} fue agregada con exito")

    def agregar_estudiante_a_actividad(self,nombre_actividad,id_estudiante):

        for m in self.lista_actividades: #Se encarga de buscar la materia dentro de la lista de actividades
            if m[0] == nombre_actividad:
                for e in self.lista_estudiantes: #Se encarga de buscar el nombre dentro de la lista de estudiantes
                    if e[0] == id_estudiante:
                        m[1].append(e)
                        print(f"\nEstudiante {e[1]} fue agregado a {m[0]}")
                        return
                    print("\nEstudiante no encontrado")
                    return
            print("\nActividad no encontrada")
            return

    def agregar_docente_a_actividad(self,nombre_actividad,id_docente):

        for m in self.lista_actividades: #Se encarga de buscar la materia dentro de la lista de actividades
            if m[0] == nombre_actividad:
                for e in self.lista_docentes: #Se encarga de buscar el nombre dentro de la lista de docentes
                    if e[0] == id_docente:
                        m[1].append(e)
                        print(f"\nDocente {e[1]} fue agregado a {m[0]}")
                        return
                    print("\nDocente no encontrado")
                    return
            print("\nActividad no encontrada")
            return

    #Metodo para mostrar las materias con sus respectivos docentes
    def mostrar_actividades_asignadas_a_estudiantes(self):

        #verifica que existan materias
        if not self.lista_actividades:
            print("\nNo hay registros de actividades")
            return
        
        #Imprime las materias existentes
        for m in self.lista_actividades:

            print(f"\nACTIVIDAD: {m[0]}")
            print("")

            if not self.lista_estudiantes: #Verifica que existan registros de estudiantes
                print("\nNo hay registros de estudiantes")
            else:
                for e in m[1]: #imprime los estudiantes correspondientes a la materia
                    print(f"\nID: {e[0]} Nombre: {e[1]}")

    #Metodo para mostrar las materias con sus respectivos docentes
    def mostrar_actividades_asignadas_a_docentes(self):

        #verifica que existan materias
        if not self.lista_actividades:
            print("\nNo hay registros de actividades")
            return
        
        #Imprime las materias existentes
        for m in self.lista_actividades:

            print(f"\nACTIVIDAD: {m[0]}")
            print("")

            if not self.lista_docentes: #Verifica que existan registros de docentes
                print("\nNo hay registros de docentes")
            else:
                for e in m[1]: #imprime los docentes correspondientes a la materia
                    print(f"\nID: {e[0]} Nombre: {e[1]}")

#Clase materia
class materia:

    #Definicion de listas
    def __init__(self):
        self.lista_estudiantes = [] #Lista para recibir la lista de estudiantes
        self.lista_docentes = [] #Lista para recibir la lista de docentes
        self.materias_dictadas = [["matematicas",[]],["ciencias",[]],["sociales",[]]] #Lista para asignar docentes a materias, con materias predefinidas
        self.materias_asignadas = [["matematicas",[],{}],["ciencias",[],{}],["sociales",[],{}]] #Lista para asignar estudiantes a materias, con materias predefinidas, tambien para asignar notas

    #Registrar notas
    def Registrar_notas(self,id_estudiante,nombre_materia,nota):

                           
        for x in self.materias_asignadas:

            if x[0] == nombre_materia: #Verifica que la materia si exista
                if not x[1]: #Verifica que haya registros de estudiantes para la materia
                    print("\nNo hay estudiantes registrados para esta materia")
                    return
                estudiantes = x[1]
                notas = x[2]
                for i in estudiantes:
                    if i[0] == id_estudiante:

                        if id_estudiante not in notas:
                            notas[id_estudiante] = []
                        
                        notas[id_estudiante].append(nota)
                        print(f"\n nota: {nota} registrada para {i[1]} en {x[0]}")
                        return
                    
                    print("\nEl estudiante no esta inscrito en la materia")
                    return
                
        print("\nMateria no encontrada")

    #Mostrar notas registradas
    def mostrar_notas(self,id_estudiante,materia):

        for m in self.materias_asignadas: #Verificar que la materia si exista
            if m[0] == materia:
                notas = m[2]

                if id_estudiante in notas: #Imprime las notas del estudiante 
                    print(f"\nNotas en materia {m[0]}:")
                    print(notas[id_estudiante])
                else:
                    print("\nNo hay notas registradas para el estudiante en esta materia")
                return
        print("\nMateria no encontrada")

    #Recibir lista de estudiantes
    def recibir_estudiantes(self,lista_estudiantes):
        self.lista_estudiantes = lista_estudiantes

    #Recibir lista de docentes
    def recibir_docentes(self,lista_docentes):
        self.lista_docentes = lista_docentes

    #Metodo para agregar nuevas materias a estudiantes
    def agregar_nuevas_materias_estudiantes(self,nombre_materia):
        for m in self.materias_asignadas:

            #Verifica que la materia ingresada no este repetida
            if m[0] == nombre_materia:
                print(f"\nLa materia {nombre_materia} ya existe")
                return
            
        self.materias_asignadas.append([nombre_materia,[],{}])
        print(f"\nLa materia {nombre_materia} fue agregada con exito.")

    #Metodo para agregar nuevas materias a docentes
    def agregar_nuevas_materias_docentes(self,nombre_materia):
        for m in self.materias_dictadas:

            #Verifica que la materia ingresada no este repetida
            if m[0] == nombre_materia:
                print(f"\nLa materia {nombre_materia} ya existe")
                return
            
        self.materias_dictadas.append([nombre_materia,[]])
        print(f"\nLa materia {nombre_materia} fue agregada con exito.")

    #Metodo para agregar estudiante a una materia
    def agregar_estudiante_a_materia(self,nombre_materia,id_estudiante):

        for m in self.materias_asignadas: #Se encarga de buscar la materia dentro de la lista de materias
            if m[0] == nombre_materia:
                for e in self.lista_estudiantes: #Se encarga de buscar el nombre dentro de la lista de estudiantes
                    if e[0] == id_estudiante:
                        m[1].append(e)
                        print(f"\nEstudiante {e[1]} fue agregado a {m[0]}")
                        return
                print("\nEstudiante no encontrado")
                return
        print("\nMateria no encontrada")
        
        
    #Metodo para agregar docente a una materia
    def agregar_docente_a_materia(self,nombre_materia,id_docente):

        for m in self.materias_dictadas: #Se encarga de buscar la materia dentro de la lista de materias
            if m[0] == nombre_materia:
                for e in self.lista_docentes: #Se encarga de buscar el nombre dentro de la lista de estudiantes
                    if e[0] == id_docente:
                        m[1].append(e)
                        print(f"\ndocente {e[1]} fue agregado a {m[0]}")
                        return
                print("\nDocente no encontrado")
                return
        print("\nMateria no encontrada")

    #Metodo para mostrar las materias con sus respectivos estudiantes            
    def mostrar_materias_asiganadas_a_estudiantes(self):

        #Verifica que existan materias
        if not self.materias_asignadas:
            print("\nNo hay registros de materias")
            return
        
        #Imprime las materias existentes
        for m in self.materias_asignadas:

            print(f"\nMATERIA: {m[0]}")
            print("")

            if not self.lista_estudiantes:#Verifica que existan registros de estudiantes 
                print("\nNo hay registros de estudiantes")
            else:
                for e in m[1]: #Imprime los estudiantes correspondientes a la materia
                    print(f"\nID: {e[0]} Nombre: {e[1]}")

    #Metodo para mostrar las materias con sus respectivos docentes
    def mostrar_materias_asignadas_a_docentes(self):

        #verifica que existan materias
        if not self.materias_dictadas:
            print("\nNo hay registros de materias")
            return
        
        #Imprime las materias existentes
        for m in self.materias_dictadas:

            print(f"\nMATERIA: {m[0]}")
            print("")

            if not self.lista_docentes: #Verifica que existan registros de docentes
                print("\nNo hay registros de docentes")
            else:
                for e in m[1]: #imprime los docentes correspondientes a la materia
                    print(f"\nID: {e[0]} Nombre: {e[1]}")

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



#---------------------Programa principal----------------------------------------------------------------

#--------instancias---------------------
Estudiante1 = Estudiante()
docente1 = docente()
materia1 = materia()
actividad1 = actividad()
biblio = biblioteca()
#---------------------------------------

print("-"*40)
print("Bienvenido al sistema académico")
print("-"*40)

# --------------------Menu de opciones------------------------------------------------------------------
while True:
    print("")
    print("-"*40)
    print("MENÚ")
    print("-"*40)
    print("Presiona:\n1. Acceder a estudiantes\n2. Acceder a docentes\n3. Acceder a biblioteca\n4. Salir del programa")
    eleccion = input("Ingresa una opción: ")

    #Verifica que se ingrese algun dato
    if eleccion == "":
        print("\n Debes ingresar una opción.")
        continue

    #Valida que sea un numero entero
    try:
        eleccion = int(eleccion)
    except ValueError:
        print("")
        print("-"*40)
        print("Ingrese un número válido.")
        print("-"*40)
        continue

    #Valida si el ususario ingresa 1 o 2
    if eleccion < 1 or eleccion > 4:
        print("")
        print("-"*40)
        print("Opción no disponible. Intente nuevamente.")
        print("-"*40)
        continue

    #Verifica opciones

    #------------menu de estudiantes--------------------------------------
    if eleccion == 1:
        print("")
        print("-"*40)
        print("Bienvenido al area de estudiantes")
        print("-"*40)
        
        while True:

            #Menu de opciones del estudiante
            print("-"*40)
            print("Sistema de estudiantes")
            print("-"*40)
            print("\nPresiona: \n1. Agregar estudiante\n2. Modificar estudiante\n3. Mostrar estudiantes\n4. Eliminar estudiante\n5. Ver las materias disponibles y estudiantes asignados a ellas\n6. Agregar una nueva materia\n7. Agregar estudiante a una materia\n8. Ver las actividades disponibles y estudiantes asignados\n9. Agregar nueva actividad\n10. Agregar estudiante a una actividad\n11. Registrar nota\n12. Mostrar notas\n13. Salir al sistema principal")
            opcion = input("\nIngresa una opcion: ")

            #verifica que la variable no este vacia
            if opcion == "":
                print("\nDebes ingresar una opción.")
                continue

            #Verifica que la variable sea un numero y lo convierte a entero
            try:
                opcion = int(opcion)
            except ValueError:
                print("")
                print("-"*40)
                print("Ingrese un número válido.")
                print("-"*40)
                continue

            #Verifica que la variable este dentro del rango de posibles opciones
            if opcion < 1 or opcion > 13:
                print("")
                print("-"*40)
                print("Opción no disponible. Intente nuevamente.")
                print("-"*40)
                continue
            
            if opcion == 1: #Agregar estudiantes
                
                Estudiante1.agregar_estudiante()
            
            elif opcion == 2: #Modificar datos de un estudiante

                Estudiante1.modificar_datos_estudiante()
            
            elif opcion == 3: #Mostrar actual de estudiantes

                mostrar_datos_estudiantes = Estudiante1.mostrar_estudiantes()

            elif opcion == 4: #Eliminar datos de un estudiante

                Estudiante1.eliminar_estudiantes()

            elif opcion == 5: #Ver las materias disponibles y estudiantes asignados a ellas
                
                materia1.mostrar_materias_asiganadas_a_estudiantes()

            elif opcion == 6: #Agregar una nueva materia
                
                nombre_materia = input("\nIngresa el nombre de la materia que deseas asignar: ")

                while not nombre_materia: #Asegura que se asigne un nombre de materia
                    nombre_materia = input("\nDebe ingresar el nombre de la materia: ")

                materia1.agregar_nuevas_materias_estudiantes(nombre_materia)

            elif opcion == 7: #Agregar un estudiante a una materia

                if not Estudiante1.obtener_lista_estudiantes():

                    print("\nNo hay estudiantes registrados")

                else:

                    id_estudiante = input("\nIngrese el id del estudiante que desea asignar: ")

                    while not id_estudiante: #Asegura que se asigne un id de estudiante
                        id_estudiante = input("\nDebe agregar el id del estudiante: ")

                    nombree_materia = input("\nIngrese el nombre de la materia a la cual desea asignar al estudiante: ")

                    while not nombree_materia: #Aegura que asigne una materia
                        nombree_materia = input("\nDebe agregar el nombre de la materia: ")

                    materia1.recibir_estudiantes(Estudiante1.obtener_lista_estudiantes()) #Obtener lista de estudiantes y pasarla como parametro
                    materia1.agregar_estudiante_a_materia(nombree_materia,id_estudiante)

            elif opcion == 8: #Ver lista de actividades disponibles y sus respectivos registros

                actividad1.mostrar_actividades_asignadas_a_estudiantes()

            elif opcion == 9: #Asignar una nueva actividad

                nombre_actividad = input("\nIngresa el nombre de la actividad que deseas agregar: ")
                while not nombre_actividad:
                    nombre_actividad = input("\nDebes agregar el nombre de la actividad: ")

                actividad1.agregar_nuevas_actividades(nombre_actividad)

            elif opcion == 10: #Asignar estudiante a una actividad

                if not Estudiante1.obtener_lista_estudiantes():

                    print("\nNo hay estudiantes registrados")

                else:

                    id_estudiante = input("\nIngrese el id del estudiante que desea asignar: ")

                    while not id_estudiante: #Asegura que se asigne un id de estudiante
                        id_estudiante = input("\nDebe agregar el id del estudiante: ")

                    nombree_actividad = input("\nIngrese el nombre de la actividad a la cual desea asignar al estudiante: ")

                    while not nombree_actividad: #Aegura que asigne una materia
                        nombree_actividad = input("\nDebe agregar el nombre de la actividad: ")

                    actividad1.recibir_estdiantes(Estudiante1.obtener_lista_estudiantes()) #Obtener lista de estudiantes y pasarla como parametro
                    actividad1.agregar_estudiante_a_actividad(nombree_actividad,id_estudiante)

            elif opcion == 11:

                if not Estudiante1.obtener_lista_estudiantes():

                    print("\nNo hay estudiantes registrados")

                else:

                    id_estudiante = input("\nIngrese el id del estudiante que desea registrar nota: ")
                    while not id_estudiante:
                        id_estudiante = input("\nDebe agregar el id del estudiante: ")

                    nombre_materia = input("\nIngrese el nombre de la materia a la cual desea asignar la nota: ")
                    while not nombre_materia:
                        nombre_materia = input("\nDebe ingresar el nombre de la materia: ")

                    nota = input("\nIngrese la nota: ")
                    while not nota:
                        nota = input("\nDebe ingresar la nota: ")

                    try:
                        nota = int(nota)

                    except ValueError:

                        print("\nTipo de dato invalido, debe ingresar un numero")
                        continue

                    materia1.Registrar_notas(id_estudiante,nombre_materia,nota)

            elif opcion == 12:  

                if not Estudiante1.obtener_lista_estudiantes():

                    print("\nNo hay estudiantes registrados")

                else:

                    id_estudiante = input("\nIngrese el id del estudiante que desea ver las notas: ")
                    while not id_estudiante:
                        id_estudiante = input("\nDebe agregar el id del estudiante: ")

                    nombre_materia = input("\nIngrese el nombre de la materia a la cual desea ver las notas: ")
                    while not nombre_materia:
                        nombre_materia = input("\nDebe ingresar el nombre de la materia: ")

                    materia1.mostrar_notas(id_estudiante,nombre_materia)

            #Volver al menu principal
            elif opcion == 13:
                print("\nSaliendo del area de estudiantes....")
                break
            
    #------------------------Menu de docentes------------------------------------------------------------------------------
    elif eleccion == 2:
        print("")
        print("-"*40)
        print("Bienvenido al area de docentes")
        print("-"*40)

        #Menu de opciones del docente
        while True:
            print("-"*40)
            print("Sistema de docentes")
            print("-"*40)
            print("\nPresiona: \n1. Agregar docente\n2. Modificar docente\n3. Mostrar docentes\n4. Eliminar docente\n5. Ver las materias disponibles y docentes asignados a ellas\n6. Agregar una nueva materia\n7. Agregar docente a una materia\n8. Ver actividades disponibles y docentes asignados a ellas\n9. Agregar nueva activiad\n10. Agregar docente a una actividad\n11. Salir al sistema principal")
            opcion = input("\nIngresa una opcion: ")

            #verifica que la variable no este vacia
            if opcion == "":
                print("\nDebes ingresar una opción.")
                continue

            #Verifica que la variable sea un numero y lo convierte a entero
            try:
                opcion = int(opcion)
            except ValueError:
                print("")
                print("-"*40)
                print("Ingrese un número válido.")
                print("-"*40)
                continue
            
            #Verifica que la variable este dentro del rango de posibles opciones
            if opcion < 1 or opcion > 11:
                print("")
                print("-"*40)
                print("Opción no disponible. Intente nuevamente.")
                print("-"*40)
                continue
            
            if opcion == 1: #Agregar un docente

                docente1.agregar_docente()
            
            elif opcion == 2: #Modificar un docente

                docente1.modificar_datos_docente()
            
            elif opcion == 3: #Mostrar los datos de los docentes 

                mostrar_datos_docentes = docente1.mostrar_docentes()

            elif opcion == 4: #Eliminar datos de un docente

                docente1.eliminar_docentes()

            elif opcion == 5: #Mostrar materias disponibles y los docentes asignados a ellas

                materia1.mostrar_materias_asignadas_a_docentes()

            elif opcion == 6: #Agregar nuevas materias
                
                nombre_materia = input("\nIngresa el nombre de la materia que deseas asignar: ")

                while not nombre_materia: #Asegura que se asigne un nombre de materia
                    nombre_materia = input("\nDebe ingresar el nombre de la materia: ")

                materia1.agregar_nuevas_materias_docentes(nombre_materia)

            elif opcion == 7: #Agregar un docente a una materia
                
                if not docente1.obtener_lista_docentes():

                    print("\nNo hay docentes registrados")

                else:

                    id_docente = input("\nIngrese el id del docente que desea asignar: ")

                    while not id_docente: #Asegura que se asigne un id de docente
                        id_docente = input("\nDebe agregar el id del docente: ")

                    nombree_materia = input("\nIngrese el nombre de la materia a la cual desea asignar al docente: ")

                    while not nombree_materia: #Aegura que asigne una materia
                        nombree_materia = input("\nDebe agregar el nombre de la materia: ")

                    materia1.recibir_docentes(docente1.obtener_lista_docentes()) #Obtener lista de docentes y pasarla como parametro
                    materia1.agregar_docente_a_materia(nombree_materia,id_docente)

            elif opcion == 8: #Mostrar lista de actividades y sus asignaciones

                actividad1.mostrar_actividades_asignadas_a_docentes()

            elif opcion == 9: #Agregar nuevas actividades

                nombre_actividad = input("\nIngresa el nombre de la actividad que deseas agregar: ")
                while not nombre_actividad:
                    nombre_actividad = input("\nDebes agregar el nombre de la actividad: ")

                actividad1.agregar_nuevas_actividades(nombre_actividad)

            elif opcion == 10: #Agregar docente a una actividad

                if not docente1.obtener_lista_docentes():

                    print("\nNo hay docentes registrados")

                else:

                    id_docente = input("\nIngrese el id del docente que desea asignar: ")

                    while not id_docente: #Asegura que se asigne un id de docente
                        id_docente = input("\nDebe agregar el id del docente: ")

                    nombree_actividad = input("\nIngrese el nombre de la actividad a la cual desea asignar al docente: ")

                    while not nombree_actividad: #Aegura que asigne una materia
                        nombree_actividad = input("\nDebe agregar el nombre de la materia: ")

                    actividad1.recibir_docentes(docente1.obtener_lista_docentes()) #Obtener lista de docentes y pasarla como parametro
                    actividad1.agregar_docente_a_actividad(nombree_actividad,id_docente)

            #Volver al menu principal
            elif opcion == 11:
                print("\nSaliendo del area de docentes....")
                break


#--------------------------sistema de biblioteca--------------------------------------------------------------------------------------
    elif eleccion == 3:

        print("-"*40)
        print("Bienvenido al sistema de biblioteca")
        print("-"*40)

        while True:
            pregunta = input("\nPresiona\n1. si eres estudiante\n2. si eres profesor\n3. Salir al programa principal: ")

            if pregunta == "":
                print("\nDebes ingresar una opción.")
                continue

            #Verifica que la variable sea un numero y lo convierte a entero
            try:
                pregunta = int(pregunta)
            except ValueError:
                print("")
                print("-"*40)
                print("Ingrese un número válido.")
                print("-"*40)
                continue
            
            #Verifica que la variable este dentro del rango de posibles opciones
            if pregunta < 1 or pregunta > 3:
                print("")
                print("-"*40)
                print("Opción no disponible. Intente nuevamente.")
                print("-"*40)
                continue

            #--------------------Biblioteca estudiantes---------------------------------------------------------------------
            if pregunta == 1:

                if not Estudiante1.obtener_lista_estudiantes():
                    print("\nNo hay registros de estudiantes")

                else:
                    while True:
                        eleccionn = input("\n¿Que deseas hacer?\n1. Mostrar biblioteca\n2. Solicitar un prestamo\n3. Devolver un objeto\n4. Mostrar prestamos\n5. Salir: ")

                        #Verifica que la variable contenga algo
                        if eleccionn == "":
                            print("\nDebes ingresar una opción.")
                            continue

                        #Verifica que la variable sea un numero y lo convierte a entero
                        try:
                            eleccionn = int(eleccionn)
                        except ValueError:
                            print("")
                            print("-"*40)
                            print("Ingrese un número válido.")
                            print("-"*40)
                            continue
            
                        #Verifica que la variable este dentro del rango de posibles opciones
                        if eleccionn < 1 or eleccionn > 5:
                            print("")
                            print("-"*40)
                            print("Opción no disponible. Intente nuevamente.")
                            print("-"*40)
                            continue

                        if eleccionn == 1: #Mostrar libros
                            
                            biblio.mostrar_libros()

                        elif eleccionn == 2: #prestar un libro
                            
                            print("\nPrestamo de objetos bibliotecarios")
                            #Solicitud de id
                            id_solicitado_estudiante = input("\nIngrese el id del estudiante: ")
                            while not id_solicitado_estudiante: #Verifica que la variable no quede vacia
                                id_solicitado_estudiante = input("\nDebe ingresar el id del estudiante: ")

                            #Solicitud de objeto bibliotecario
                            libro_solicitado = input("\nIngrese el objeto bibliotecario que desea adquirir: ")
                            while not libro_solicitado: #Verifica que la variable no quede vacia
                                libro_solicitado = input("\nDebe ingresar un objeto bibliotecario: ")

                            buscar_estudiante = Estudiante1.buscar_estudiante(id_solicitado_estudiante)

                            biblio.prestamo_estudiante(buscar_estudiante,libro_solicitado)

                        elif eleccionn == 3: #devolver un libro

                            print("\nDevolucion de objetos bibliotecarios")
                            #Solicitud de id
                            id_solicitado_estudiante = input("\nIngrese el id del estudiante: ")
                            while not id_solicitado_estudiante: #Verifica que la variable no quede vacia
                                id_solicitado_estudiante = input("\nDebe ingresar el id del estudiante: ")

                            #Solicitud de objeto bibliotecario
                            libro_solicitado = input("\nIngrese el objeto bibliotecario que desea devolver: ")
                            while not libro_solicitado: #Verifica que la variable no quede vacia
                                libro_solicitado = input("\nDebe ingresar un objeto bibliotecario: ")

                            buscar_estudiante = Estudiante1.buscar_estudiante(id_solicitado_estudiante)

                            biblio.devolucion_estudiante(buscar_estudiante,libro_solicitado)

                        elif eleccionn == 4 : #Mostrar prestamos

                            biblio.mostrar_prestamos()

                        elif eleccionn == 5: #salir
                            print("\nSaliendo...")
                            break

            #---------------------------Biblioteca docentes------------------------------------------------------------
            elif pregunta == 2:

                if not docente1.obtener_lista_docentes():
                    print("\nNo hay registros de docentes")

                else:
                    while True:
                        eleccionn = input("\n¿Que deseas hacer?\n1. Mostrar biblioteca\n2. Solicitar un libro\n3. Devolver un libro\n4. Mostrar prestamos\n5. Salir: ")

                        #Verifica que la variable contenga algo
                        if eleccionn == "":
                            print("\nDebes ingresar una opción.")
                            continue

                        #Verifica que la variable sea un numero y lo convierte a entero
                        try:
                            eleccionn = int(eleccionn)
                        except ValueError:
                            print("")
                            print("-"*40)
                            print("Ingrese un número válido.")
                            print("-"*40)
                            continue
            
                        #Verifica que la variable este dentro del rango de posibles opciones
                        if eleccionn < 1 or eleccionn > 5:
                            print("")
                            print("-"*40)
                            print("Opción no disponible. Intente nuevamente.")
                            print("-"*40)
                            continue

                        if eleccionn == 1: #Mostrar libros
                            
                            biblio.mostrar_libros()

                        elif eleccionn == 2: #prestar un libro

                            print("\nPrestamo de objetos biblioetcarios")
                            #Solicitud de id
                            id_solicitado_docente = input("\nIngrese el id del docente: ")
                            while not id_solicitado_docente: #Verifica que la variable no quede vacia
                                id_solicitado_docente = input("\nDebe ingresar el id del docente: ")

                            #Solicitud de objeto bibliotecario
                            libro_solicitado = input("\nIngrese el objeto bibliotecario que desea adquirir: ")
                            while not libro_solicitado: #Verifica que la variable no quede vacia
                                libro_solicitado = input("\nDebe ingresar un objeto bibliotecario: ")

                            buscar_docente = docente1.buscar_docente(id_solicitado_docente)

                            biblio.prestamo_docente(buscar_docente,libro_solicitado)

                        elif eleccionn == 3: #devolver un libro

                            print("\nDevolucion de objetos bibliotecarios")
                            #Solicitud de id
                            id_solicitado_docente = input("\nIngrese el id del docente: ")
                            while not id_solicitado_docente: #Verifica que la variable no quede vacia
                                id_solicitado_docente = input("\nDebe ingresar el id del docente: ")

                            #Solicitud de objeto bibliotecario
                            libro_solicitado = input("\nIngrese el objeto bibliotecario que desea devolver: ")
                            while not libro_solicitado: #Verifica que la variable no quede vacia
                                libro_solicitado = input("\nDebe ingresar un objeto bibliotecario: ")

                            buscar_docente = docente1.buscar_docente(id_solicitado_docente)

                            biblio.devolucion_docente(buscar_docente,libro_solicitado)

                        elif eleccionn == 4: #Mostrar prestamos

                            biblio.mostrar_prestamos()

                        elif eleccionn == 4: #salir
                            print("\nSaliendo...")
                            break

            #----------------------------Finalizar sistema bibliotecario----------------------------

            elif pregunta == 3:
                print("\nSaliendo del sistema bibliotecario")
                break

    #-------------------Finalizar programa-----------------------------------------------------------
    elif eleccion == 4:
        print("\nGracias por usar el programa, hasta luego :)")
        break