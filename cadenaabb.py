import re

def verificar_secuencia(cadena):
    patron = r'^[ab]*abb$'

    if re.match(patron, cadena):
        return ("Cadena Aceptada")
    else:
        return ("Cadena rechazada")

cadena_usuario = input("Ingresa una cadena: ")

resultado = verificar_secuencia(cadena_usuario)
print(f"La cadena '{cadena_usuario}' cumple con la secuencia: {resultado}")