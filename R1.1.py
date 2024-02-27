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