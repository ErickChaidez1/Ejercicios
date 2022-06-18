
NumCemento = input("Ingresa el numero de costales de cemento: ")
NumYeso = input ("Ingresa el numero de costales de yeso: ")

KgCemento = int(NumCemento) * 40
kgYeso = int(NumYeso) * 30
CapacidadCamion = 3254


SumaKG = int(kgYeso) + int(KgCemento)

if SumaKG > CapacidadCamion :
    print ("El peso total en Kg es: " + str(SumaKG))
    print ("No se puede realizar el envio, excede la capacidad")
elif SumaKG > CapacidadCamion/2:
    print ("El peso total en Kg es: " + str(SumaKG))
    print ("Se puede realizar el envio")
elif SumaKG < CapacidadCamion/2:
    print ("El peso total en Kg es: " + str(SumaKG))
    print("No se puede realizar el envio, menor al 50% de la capacidad")





