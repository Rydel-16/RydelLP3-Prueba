
#Autor: Isabella Caballero  Moreno
#Ejercicio que permita 
def determinar_aprobado(promedio):
  
    if promedio>=11:
        resultado="Aprobado"
    else:
        resultado="Desaprobado"
    return resultado

promedio=int(input("Promedio: "))
print(determinar_aprobado(promedio))