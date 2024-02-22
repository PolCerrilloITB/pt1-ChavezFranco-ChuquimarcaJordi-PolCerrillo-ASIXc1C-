import random

def desordenar_palabra(palabra):
    if len(palabra) <= 3:
        return palabra
    else:
        primera_letra = palabra[0]
        ultima_letra = palabra[-1]
        letras_intermedias = list(palabra[1:-1])
        random.shuffle(letras_intermedias)
        palabra_desordenada = ''.join([primera_letra] + letras_intermedias + [ultima_letra])
        return palabra_desordenada

def desordenar_frase(frase):
    palabras = frase.split()
    palabras_desordenadas = [desordenar_palabra(palabra) for palabra in palabras]
    frase_desordenada = ' '.join(palabras_desordenadas)
    return frase_desordenada

def main():
    frase_original = input("Introduce una frase: ")
    frase_desordenada = desordenar_frase(frase_original)
    print("Frase original:", frase_original)
    print("Frase desordenada:", frase_desordenada)

if __name__ == "__main__":
    main()
