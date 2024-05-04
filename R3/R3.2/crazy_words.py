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
numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
caracteres = ['.', ',', '!', '?', ';', ':', '¿', '¡', '(', ')', '"', '=', '€', '/']

from crazy_phrase import frase_larga
import random
def leer_palabras(frase):
    fraseSplit = frase.split()
    frase_final = ""
    for palabra in fraseSplit:
        if len(palabra) <= 2 or (len(palabra) == 4 and palabra[-1] in caracteres):
            frase_final += palabra + " "
        elif palabra[0] in numeros or (palabra[0] in caracteres and palabra[2] in numeros) or ("." in palabra and palabra[-1]!= "." and palabra[0]!= ".") or palabra[1:-1] == palabra[1:-1][::-1]:
            frase_final += palabra + " "
        elif len(palabra) > 3:
            frase_final = frase_larga(palabra, frase_final)
        else:
            frase_final += palabra + " "
    return frase_final.strip()
def apostrofe_guion(palabra):
    if "'" in palabra or "-" in palabra:
        if "'" in palabra:
            palabra = palabra.replace("'", "").replace("'", "")
        elif "-" in palabra:
            palabra = palabra.replace("-", "").replace("-", "")
    if len(palabra) > 1 and palabra[-1] in ["'", "-"]:
        palabra = palabra[:-1] + palabra[-1] + palabra[-1]
    return palabra
def mezcla(palabra):
    palabra_inicial = palabra
    if len(palabra) != 3 and (len(palabra) != 4 or palabra[1] != palabra[2]):
        if palabra[1:-1] != palabra[1:-1][::-1]:
            while palabra == palabra_inicial:
                palabra = ''.join([palabra[0]] + random.sample(palabra[1:-1], len(palabra[1:-1])) + [palabra[-1]])
    palabra = apostrofe_guion(palabra)
    return palabra
