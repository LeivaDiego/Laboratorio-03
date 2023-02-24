def complemento_uno(numero):
    complemento = "".join(["1" if bit == "0" else "0" for bit in numero])
    return complemento


def complemento_dos(numero):
    complemento = complemento_uno(numero)
    valor = int(complemento, 2) + 1
    valor_binario = "{0:b}".format(valor).zfill(8)
    return valor_binario


while True:
    opcion = input("Seleccione una opción:\n[1] Conversion de Binarios \n[2] Conversion de Hexadecimales o decimales\n")
    if opcion == "1":
        print("Ha seleccionado Conversion de binarios")
        numero_binario = input("Ingresa un número binario de 8 bits: ")
        while len(numero_binario) != 8 or not all([bit in ["0", "1"] for bit in numero_binario]):
            print("El número ingresado no es un número binario válido de 8 bits.")
            numero_binario = input("Ingresa un número binario de 8 bits: ")

        complemento_uno_binario = complemento_uno(numero_binario)
        complemento_dos_binario = complemento_dos(numero_binario)

        print("Complemento a uno:", complemento_uno_binario)
        print("Complemento a dos:", complemento_dos_binario)
        break
    elif opcion == "2":
        print("Ha seleccionado Conversion de Hexadecimales o Decimales")
        while True:
            numero = input("Ingresa un número decimal o hexadecimal: \n no importa si es mayuscula o minuscula\n")
            if numero.isdigit():  # Si es decimal
                decimal = int(numero)
                hexadecimal = hex(decimal)[2:].upper()  # Elimina el prefijo 0x
                print(f"{decimal} en hexadecimal es {hexadecimal}")
                break
            elif all(c in "0123456789abcdefABCDEF" for c in numero):  # Si es hexadecimal
                hexadecimal = numero.upper()
                decimal = int(hexadecimal, 16)
                print(f"{hexadecimal} en decimal es {decimal}")
                break
            else:  # Si no es un número válido
                print("El número ingresado no es un número decimal o hexadecimal válido.")
        break
    else:
        print("La opción seleccionada no es válida. Por favor, ingresa 1 o 2.")

print("\n Programa finalizado")