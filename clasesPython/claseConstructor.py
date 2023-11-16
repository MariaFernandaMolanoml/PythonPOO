class Estudiante1: #Definicion de la clase Estudiante1

     #Constructor de la clase que se ejecuta al crear una instancia
    def __init__(self, codigo, nombre,apellido):
        # Iniciamos los atributos de la instancia con los valores proporcionados
        self.codigo = codigo
        self.nombre = nombre
        self.apellido=apellido
    #Metodo para imprimir la informacion del estudiante
    def imprimir_Informacion(self):
        #Imprimir los atributos de la instancia
        print (self.codigo, self.nombre, self.apellido)

         
         
adso1 =Estudiante1(2,'Maria','Fernanda') #Crear un objeto de la clase Estudiante1 llamado adso1
adso1.imprimir_Informacion() #Llamar al metodo imprimir_Informacion del objeto adso1



