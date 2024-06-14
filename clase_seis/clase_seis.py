'''
sacar el promedio de 3 edades
'''
lista_de_edades = []
acumulador = 0
bandera = False
#agrego las edades
for i in range(5):
    
    edad = input("ingresa la edad: ")
    edad = int(edad)
    lista_de_edades.append(edad)
    acumulador += edad
#promedio
promedio_edad = acumulador / len(lista_de_edades)

#determinar el mayor y menor
edad_minima = lista_de_edades[0]
for i in range(len(lista_de_edades)): #recorro desde 0 hasta la cantidad de edades que cargue, esta recorriendo los indices, no por datos, si quiero por los datos es for edad in lista_de_edades
    if bandera == False or lista_de_edades [i] > edad_maxima:
        edad_maxima = lista_de_edades[i]
        bandera = True  
    if lista_de_edades[i] < edad_minima:
        edad_minima = lista_de_edades[i]

for i in range(len(lista_de_edades)):
    print(lista_de_edades[i])

print(f"el promedio es {promedio_edad}")
print(f"la edad minima es {edad_minima}")
print(f"la edad maxima es {edad_maxima}")