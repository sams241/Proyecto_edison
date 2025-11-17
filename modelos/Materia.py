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