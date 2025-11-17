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