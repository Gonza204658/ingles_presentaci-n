# Mensaje de bienvenida al sistema del parqueadero
print("************BIENBENIDOS AL PARQUEADERO DEL ALEGRA*******************")

# Mensaje indicando que el usuario debe escoger su medio de transporte
print("************DIGITE SU MEDIO DE TRANSPORTE********************")

# Opciones del menú
print("1. CARRO ")
print("2. MOTO  ")
print("3. SALIR")

# Número inicial de carros que ya están dentro del parqueadero
Carros_adentro = 5

# Contador de carros que ingresan durante la ejecución del programa
Carros_ingresan = 0

# Número inicial de motos que ya están dentro del parqueadero
motos_adentro = 5

# Contador de motos que ingresan durante la ejecución del programa
motos_ingresan = 0

# Variable que controla si el programa sigue ejecutándose
activador = 1

# Ciclo principal del programa. Mientras activador sea 1 el sistema seguirá funcionando
while activador == 1:

    # El usuario selecciona el medio de transporte escribiendo un número
    Opcion = int(input("************************ SELECCIONA TÚ MEDIO DE TRANSPORTE ********************* "))
   
    # Si el usuario selecciona la opción 1 (CARRO)
    if Opcion == 1:

        # Se calcula el total actual de carros en el parqueadero
        total_carro = Carros_adentro + Carros_ingresan

        # Se verifica si el parqueadero de carros ya está lleno
        if total_carro >= 10:
            print("****************PARQUEADERO DE CARROS LLENO************")

        else:
            # Se solicita al usuario ingresar la placa del carro
            carro = input("¡¡HOLA!! INGRESE LA PLACA DE TÚ CARRO SIN ESPACIOS: ")

            # Se verifica que la placa tenga exactamente 6 caracteres
            if len(carro) != 6:
              print("NUMERO DE PLACA INCOMPLETO")

            else:
             # Si la placa es válida se incrementa el contador de carros ingresados
             Carros_ingresan += 1

             # Se vuelve a calcular el total de carros dentro del parqueadero
             total_carro = Carros_adentro + Carros_ingresan

             # Se muestra al usuario su número de puesto en el parqueadero
             print(f"Eres el carro número {total_carro}, PUEDE INGRESAR, ¡GRACIAS!")

    # Si el usuario selecciona la opción 2 (MOTO)
    elif Opcion == 2:

        # Se calcula el total actual de motos en el parqueadero
        total_moto = motos_adentro + motos_ingresan

        # Se verifica si el parqueadero de motos ya está lleno
        if total_moto >= 10:
            print("************PARQUEADERO DE MOTOS LLENO********" )

        else:
            # Se solicita al usuario ingresar la placa de la moto
            moto = input("¡¡HOLA!! INGRESA LA PLACA DE TÚ MOTO SIN ESPACIOS: ")

            # Se valida que la placa tenga 6 caracteres
            if len(moto) != 6:
              print("INGRESA LOS 6 DIGITOS DE LA PLACA")

            else: 
             # Si la placa es válida se incrementa el contador de motos ingresadas
             motos_ingresan += 1

             # Se calcula nuevamente el total de motos dentro del parqueadero
             total_moto = motos_adentro + motos_ingresan

             # Se muestra el puesto asignado a la moto
             print(f"Moto registrada correctamente, eres el puesto: {total_moto}, PUEDE INGRESAR, ¡GRACIAS!")

    # Si el usuario selecciona la opción 3
    elif Opcion == 3:

        # Se cambia el valor de activador a 0 para detener el ciclo
        activador = 0

        # Mensaje indicando que el usuario salió del programa
        print("SALISTE DEL PROGRAMA")

    # Si el usuario escribe una opción diferente a 1, 2 o 3
    else:
     print("Opción no válida")




     # EXPLICACION DE LINEAS DE CODIGO EN INGLES

#      print("************BIENBENIDOS AL PARQUEADERO DEL ALEGRA*******************")
# Carros_adentro = 5
# Carros_ingresan = 0
# motos_adentro = 5
# motos_ingresan = 0
# activador = 1

# while activador == 1:
#     Opcion = int(input("SELECCIONA TÚ MEDIO DE TRANSPORTE: "))
#     if Opcion == 1:
#         total_carro = Carros_adentro + Carros_ingresan

