import csv

#Clase para manejar la persistencia de los datos
class sistema_guardado:

    #Metodo constructor
    def __init__(self,gestor_estudiantes,gestor_docentes,gestor_materias,gestor_actividad,gestor_biblioteca): #Toma como parametros las instancias de las otras clases, esto para poder acceder a sus listas

        self.gestor_estudiantes = gestor_estudiantes
        self.gestor_docentes = gestor_docentes
        self.gestor_materias = gestor_materias
        self.gestor_actividad = gestor_actividad
        self.gestor_biblioteca = gestor_biblioteca

    #Metodo para guardar los libros
    def guardar_libros(self):
        with open("libros.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["nombre_libro", "disponible"])

            for libro in self.gestor_biblioteca.lista_libros:
                writer.writerow(libro)

    #Metodo para guardar la lista de los estudiantes con sus datos
    def guardar_estudiante(self):
        with open("estudiantes.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["id", "nombre", "telefono", "correo","direccion"])

            for e in self.gestor_estudiantes.lista_estudiantes:
                writer.writerow(e)

    #Metodo para guardar la lista de los docentes con sus datos
    def guardar_docente(self):
        with open("docentes.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["id", "nombre", "telefono", "correo","direccion"])

            for e in self.gestor_docentes.lista_docentes:
                writer.writerow(e)

    #Metodo para guardar los nombres de las materias
    def guardar_materias(self):
        with open("materias.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["nombre_materia"])

            for m in self.gestor_materias.materias_asignadas:
                writer.writerow([m[0]])

    #Metodo para guardar los estudiantes registrados a las materias
    def guardar_estudiantes_materia(self):
        with open("materias_estudiantes.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["materia", "id_estudiante", "nombre_estudiante"])

            for m in self.gestor_materias.materias_asignadas:
                materia = m[0]
                estudiantes = m[1]

                for est in estudiantes:
                    writer.writerow([materia, est[0], est[1]])

    #Metodo para guardar los estudiantes asigandos a actividades
    def guardar_actividad(self):
        with open("Actividades.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Actividad", "id_persona", "nombre_persona"])

            for m in self.gestor_actividad.lista_actividades:
                actividad = m[0]
                personas = m[1]

                for est in personas:
                    writer.writerow([actividad,est[0],est[1]])

    #Metodo para guardar los docentes asignados a las materias
    def guardar_docentes_materia(self):
        with open("materias_docentes.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["materia", "id_docente", "nombre_docente"])

            for m in self.gestor_materias.materias_dictadas:
                materia = m[0]
                docentes = m[1]

                for docente in docentes:
                    writer.writerow([materia,docente[0],docente[1]])

    #Metodo para guardar las notas del estudiante
    def guardar_notas(self):
        with open("notas.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["materia", "id_estudiante", "nota"])

            for m in self.gestor_materias.materias_asignadas:
                nombre_materia = m[0]
                notas = m[2]

                for id_estudiante, lista_notas in notas.items():
                    for n in lista_notas:
                        writer.writerow([nombre_materia,id_estudiante,n])

    #Metodo para guardar todos los datos
    def guardar_todo(self):
        self.guardar_estudiante()
        self.guardar_docente()
        self.guardar_materias()
        self.guardar_estudiantes_materia()
        self.guardar_notas()
        self.guardar_docentes_materia()
        self.guardar_actividad()
        self.guardar_libros()