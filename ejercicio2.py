def contar_vocales_consonantes(palabra):
    contador_vocales = 0
    contador_consonantes = 0
    vocales = "aeiouAEIOU"

    for letra in palabra:
        if letra.isalpha():
            if letra in vocales:
                contador_vocales = contador_vocales + 1
            else:
                contador_consonantes = contador_consonantes + 1

    return contador_vocales, contador_consonantes

def main():
    palabras = []
    while True:
        palabra = input("Ingresa una palabra (o presione Enter para finalizar): ")
        if not palabra:
            break
        palabras.append(palabra)

    for palabra in palabras:
        vocales, consonantes = contar_vocales_consonantes(palabra)
        print("La palabra ", palabra, " tiene ", vocales, " vocales y ", consonantes, " consonantes")

if __name__ == "__main__":
    main()
