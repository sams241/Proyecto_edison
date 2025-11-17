class Persona:

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