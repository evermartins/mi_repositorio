#Ejercicio de clase. Hacer una clase Alumno, con nombre y nota, con un método imprimir()
#Crear una instancia de Alumno, mostrando sus datos y llamando al método desde otro módulo

class Alumno:

    def __init__(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota

    def __str__(self):
        return f"Nombre: " + self.nombre +","+"Nota: "+ str(self.nota)

    def imprimir(self):
        print(f"Hola soy el alumno {self.nombre} y mi nota es {self.nota}")

