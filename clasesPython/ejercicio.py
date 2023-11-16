class Estudiante: #Definimos clase Estudiante

    #Agregamos los atributos de la clase
    codigo=0
    nombre=""
    apellido=""

    def imprimir_Datos(self,codigo,nombre,apellido): #Metodo para imprimir los datos del estudiantes

        print(self.codigo, self.nombre, self.apellido) #Imprimimos los atributos de la instancia

#crear objeto adso
adso=Estudiante()

#Asignar valores a los atributos del objeto
adso.codigo = 1
adso.nombre = 'Sandra'
adso.apellido='Cruz'

adso.imprimir_Datos() #Llamar al metodo imprimir_Datos del objeto adso
