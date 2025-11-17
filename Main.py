from modelos.Estudiante import Estudiante
from modelos.Docente import docente
from modelos.Actividad import actividad
from modelos.Materia import materia
from modelos.Biblioteca import biblioteca
from modelos.Sistema_guardado import sistema_guardado

#---------------------Programa principal----------------------------------------------------------------

#--------instancias---------------------
Estudiante1 = Estudiante()
docente1 = docente()
materia1 = materia()
actividad1 = actividad()
biblio = biblioteca()
guardador = sistema_guardado(Estudiante1,docente1,materia1,actividad1,biblio)
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
    print("Presiona:\n1. Acceder a estudiantes\n2. Acceder a docentes\n3. Acceder a biblioteca\n4. Guardar datos en csv\n5. Salir del programa")
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

    
    elif eleccion == 4:
        print("-"*40)
        print("Guardando datos....")
        print("-"*40)

        guardador.guardar_todo()

        print("\nDatos guardados con exito :)")

    #-------------------Finalizar programa-----------------------------------------------------------
    elif eleccion == 5:
        print("\nGracias por usar el programa, hasta luego :)")
        break