print("==========================================================")
Cajas = int(input ("Ingrese la cantidad de cajas a vender: "))
ID = int(input("Ingrese el ID del producto: "))


Caja1 = 285.55
Caja2 = 334.72
Caja3 = 129.00
Envio = 1500

if Cajas <= 100:
    if ID == 1:
        print("======================================")
        print("El producto es Maíz grano")
        print("El precio por caja es $" + str(Caja1))

        total = int(Caja1) * int(Cajas) + int(Envio)
        print("El costo total a pagar son: $" + str(total))
        print("======================================")
    elif ID == 2:
        print("======================================")
        print("El producto es Pepino")
        print("El precio por caja es $" + str(Caja2))

        total = int(Caja2) * int(Cajas) + int(Envio)
        print("El costo total a pagar son: $" + str(total))
        print("======================================")
    elif ID == 3:
        print("======================================")
        print("El producto es Tomate verde")
        print("El precio por caja es $" + str(Caja3))

        total = int(Caja3) * int(Cajas) + int(Envio)
        print("El costo total a pagar son: $" + str(total))
        print("======================================")
else :
    print("=====================================================================")
    print("Las cajas exceden de 100 por lo cual no se puede realizar la venta")
    print("=====================================================================")
