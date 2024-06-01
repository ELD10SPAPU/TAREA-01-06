

def contar_vocales_consonantes(palabra):
    contador_vocales = 0
    contador_consonantes = 0
    vocales = "aeiou"

    palabra=input("Ingrese una palabra")
    
    for letra in palabra.lower():
        if letra.isalpha():
            if letra in vocales:
                contador_vocales += 1
            else:
                contador_consonantes += 1

    return contador_vocales, contador_consonantes