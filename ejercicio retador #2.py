Cont = 0
municipios = [1,2,3], [1,2,3]

while Cont<3 :
    
    municipios[0][Cont]= input("Ingresa un municipio: ")
    municipios[1][Cont] = input ("Ingresa los habitantes del municipio: ")
    Cont +=1

HabitantesTotal = int(municipios[1][0]) + int(municipios[1][1]) + int(municipios[1][2]) 
Promedio = (HabitantesTotal / 3)

print("La sumatoria es: " + str(HabitantesTotal))
print("El promedio es: " + str(Promedio))