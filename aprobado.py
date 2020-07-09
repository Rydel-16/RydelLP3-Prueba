#Autor:Chalque Miñope Rydel



def determinaraprobado(promedio):
    if promedio>=11:
        resultado = "Aprobado"
    else:
        resultado = "Desaprobado"
    return resultado
promedio= int(input("Promedio:  "))
print(determinaraprobado(promedio))    
