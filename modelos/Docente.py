from modelos.Persona import Persona

class docente(Persona):

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

    def buscar_docente(self,id_docente):
        for x in self.lista_docentes:
            if x[0] == id_docente:
                return x
        return None