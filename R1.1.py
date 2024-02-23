import random

def desordenar_palabra(palabra):
    if len(palabra) > 2:
        inicio = palabra[0]
        final = palabra[-1]
        intermedio = list(palabra[1:-1])
        random.shuffle(intermedio)
        palabra_desordenada = inicio + ''.join(intermedio) + final
        return palabra_desordenada
    else:
        return palabra

def desordenar_texto(frase):
    palabras = frase.split()
    palabras_desordenadas = [desordenar_palabra(palabra) for palabra in palabras]
    return ' '.join(palabras_desordenadas)

def main():
    frase = input("")
    frase_desordenada = desordenar_texto(frase)
    print("", frase_desordenada)

main()