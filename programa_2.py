#Este programa sirve para saber el mayor de tres numeros
def programa():
    #Cada num 1/2/3 es una asignacion
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enetr second number: "))
    num3 = float(input("Enter third number: "))
    i= input
    #i variable acumuladora
    #for bucle
    for i in range(10):
        #Condicional
        if  (num1 >= num2) and (num1 >= num3):
            x = num1
        else:
            if  (num2 >= num1) and (num2 >= num3):
              x = num2  
            else:
                x = num3
    print "El numero mayor es", x

programa()

