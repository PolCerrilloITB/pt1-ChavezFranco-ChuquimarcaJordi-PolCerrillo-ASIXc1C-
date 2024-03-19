'''
Franco Chavez/Jordi Chuquimarca/Pol Cerrillo
19/03/2023
ASIXc1C M03 UF2
Descripción: Partint del problema general cal dividir-lo en problemes més simples, denominats subproblemes.
Així trobarem les funcions en les quals cal descompondre.
Un punt important, a tenir en compte en aplicar aquesta descomposició, és que cadascun dels subproblemes
no es genera arbitràriament, sinó que es planteja com un objectiu parcial, amb entitat pròpia, per resoldre
el seu problema de nivell superior. Un cop assolits tots aquests objectius parcials, es considera resolt el total.
'''
import random
def demanar_frase():
    frase = str(input(""))
    frase_mezcla = desordenar_texto(frase)
    print(frase_mezcla)
    return demanar_frase
def numero(palabra):
    try:
        int(palabra)
        return True
    except ValueError:
        return False
def desordenar_palabra(palabra):
    if len(palabra) > 2:
        if numero(palabra):
            return palabra
        simbolos = ',.?¿¡!;:€@/()=&%$#"|'
        if palabra[-1] in simbolos:
            simbolos = palabra[-1]
            palabra = palabra[:-1]
            intermedio = list(palabra[1:-1])
            random.shuffle(intermedio)
            desorden = palabra[0] + ''.join(intermedio) + palabra[-1] + simbolos
        elif palabra[0] in simbolos:
            simbolos = palabra[0]
            palabra = palabra[0:]
            intermedio = list(palabra[2:-1])
            random.shuffle(intermedio)
            desorden = simbolos + palabra[1] + ''.join(intermedio) + palabra[-1]
        elif palabra[:] in simbolos:
            palabra = palabra[:]
            intermedio = list(palabra[:])
            desorden = palabra[0] + intermedio + palabra[-1]
        else:
            intermedio = list(palabra[1:-1])
            random.shuffle(intermedio)
            desorden = palabra[0] + ''.join(intermedio) + palabra[-1]
        return desorden
    else:
        return palabra
def desordenar_texto(frase):
    palabras = frase.split()
    mezcla = [desordenar_palabra(palabra) for palabra in palabras]
    frase_mezcla = ' '.join(mezcla)
    return frase_mezcla
