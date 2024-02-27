'''
Franco Chavez/Jordi Chuquimarca/Pol Cerrillo
27/02/2023
ASIXc1C M03 UF2
Descripción: Partint del problema general cal dividir-lo en problemes més simples, denominats subproblemes.
Així trobarem les funcions en les quals cal descompondre.
Un punt important, a tenir en compte en aplicar aquesta descomposició, és que cadascun dels subproblemes
no es genera arbitràriament, sinó que es planteja com un objectiu parcial, amb entitat pròpia, per resoldre
el seu problema de nivell superior. Un cop assolits tots aquests objectius parcials, es considera resolt el total.
'''
import random
import string


def es_numero(palabra):
    try:
        float(palabra)
        return True
    except ValueError:
        return False


def desordenar_palabra(palabra):
    if len(palabra) > 2:
        if es_numero(palabra):
            return palabra

        simbolos_puntuacion = string.punctuation
        puntuacion_inicio = ''
        puntuacion_final = ''

        if palabra[0] in simbolos_puntuacion:
            puntuacion_inicio = palabra[0]
            palabra = palabra[1:]
        if palabra[-1] in simbolos_puntuacion:
            puntuacion_final = palabra[-1]
            palabra = palabra[:-1]

        if len(palabra) > 2:
            intermedio = list(palabra[1:-1])
            random.shuffle(intermedio)
            palabra_desordenada = palabra[0] + ''.join(intermedio) + palabra[-1]
        else:
            palabra_desordenada = palabra

        return puntuacion_inicio + palabra_desordenada + puntuacion_final
    else:
        return palabra


def desordenar_texto(frase):
    palabras = frase.split()
    mezcla = [desordenar_palabra(palabra) for palabra in palabras]
    frase_mezcla = ' '.join(mezcla)
    return frase_mezcla


def main():
    frase = str(input("Ingrese una frase: "))
    frase_mezcla = desordenar_texto(frase)
    print(frase_mezcla)


main()
