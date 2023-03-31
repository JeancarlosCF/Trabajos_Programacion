def decodificar_Cesar(mensaje, corrimiento):
    mensaje_Descifrado = ""
    for caracter in mensaje:
        if not caracter.isalpha():
            mensaje_Descifrado += caracter
            continue

        ascii_original = ord(caracter)
        ascii_nuevo = ascii_original - corrimiento

        if caracter.isupper():
            if ascii_nuevo < ord('A'):
                ascii_nuevo += 26
            elif ascii_nuevo > ord('Z'):
                ascii_nuevo -= 26
                
        elif caracter.islower():
            if ascii_nuevo < ord('a'):
                ascii_nuevo += 26
            elif ascii_nuevo > ord('z'):
                ascii_nuevo -= 26

        caracter_Descifrado = chr(ascii_nuevo)
        mensaje_Descifrado += caracter_Descifrado

    return mensaje_Descifrado

mensaje_Codificado = input("Digite mensaje codificado: ") #Ejemplo: Krod Pxqgr (Hola mundo)
corrimiento = 3 #Mensaje codificados con corrimiento de letas de 3

mensaje_Descifrado = decodificar_Cesar(mensaje_Codificado, corrimiento)

print(mensaje_Descifrado)