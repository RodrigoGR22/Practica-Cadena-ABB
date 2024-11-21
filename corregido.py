def verificar_secuencia(cadena):
    if cadena.endswith("abb"):
        for char in cadena[:-3]:
            if char not in 'ab':
                return "Cadena rechazada"
        return "Cadena Aceptada"
    else:
        return "Cadena rechazada"

cadena_usuario = input("Ingresa una cadena: ")
resultado = verificar_secuencia(cadena_usuario)
print(f"La cadena '{cadena_usuario}' cumple con la secuencia: {resultado}")
