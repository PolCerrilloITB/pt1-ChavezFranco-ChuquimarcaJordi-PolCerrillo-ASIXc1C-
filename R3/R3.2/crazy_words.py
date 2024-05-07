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

import random

# Función para procesar palabras en una frase.
def leer_palabras(frase):
    # Divide la frase en palabras.
    fraseSplit = frase.split()
    frase_final = ""
    for palabra in fraseSplit:
        # Condiciones para mantener la palabra sin cambios.
        if len(palabra) <= 2 or (len(palabra) == 4 and palabra[-1] in caracteres):
            frase_final += palabra + " "
        # Condiciones para mantener la palabra sin cambios o con modificaciones específicas.
        elif palabra[0] in numeros or (palabra[0] in caracteres and palabra[2] in numeros) or ("." in palabra and palabra[-1]!= "." and palabra[0]!= ".") or palabra[1:-1] == palabra[1:-1][::-1]:
            frase_final += palabra + " "
        # Si la palabra es más larga que 3 caracteres, se procesa.
        elif len(palabra) > 3:
            frase_final = procesar_palabra(palabra, frase_final)
        else:
            frase_final += palabra + " "
    return frase_final.strip()

# Función para procesar una palabra específica.
def procesar_palabra(palabra, frase):
    palabra_modificada = palabra
    # Modifica la palabra según la posición de caracteres especiales.
    if palabra[-1] in caracteres and palabra[0] in caracteres:
        primer_caracter = palabra[0]
        ultimo_caracter = palabra[-1]
        palabra_modificada = palabra_modificada[1:-1]
        palabra_modificada = mezcla(palabra_modificada)
        palabra_modificada = primer_caracter + palabra_modificada + ultimo_caracter
    elif palabra[-1] in caracteres:
        ultimo_caracter = palabra[-1]
        palabra_modificada = palabra_modificada[:-1]
        palabra_modificada = mezcla(palabra_modificada) + ultimo_caracter
    elif palabra[0] in caracteres and palabra[-1] in caracteres:
        primer_caracter = palabra[0]
        palabra_modificada = palabra_modificada[1:]
        palabra_modificada = primer_caracter + mezcla(palabra_modificada)
    else:
        palabra_modificada = mezcla(palabra_modificada)

    # Agrega la palabra modificada a la frase.
    frase += palabra_modificada + " "
    return frase

# Función para procesar apóstrofos y guiones en palabras.
def apostrofe_guion(palabra):
    if "'" in palabra or "-" in palabra:
        if "'" in palabra:
            palabra = palabra.replace("'", "").replace("'", "")
        elif "-" in palabra:
            palabra = palabra.replace("-", "").replace("-", "")
    if len(palabra) > 1 and palabra[-1] in ["'", "-"]:
        palabra = palabra[:-1] + palabra[-1] + palabra[-1]
    return palabra

# Función para mezclar las letras de una palabra, manteniendo los caracteres especiales en su lugar.
def mezcla(palabra):
    palabra_inicial = palabra
    if len(palabra) != 3 and (len(palabra) != 4 or palabra[1] != palabra[2]):
        if palabra[1:-1] != palabra[1:-1][::-1]:
            while palabra == palabra_inicial:
                palabra = ''.join([palabra[0]] + random.sample(palabra[1:-1], len(palabra[1:-1])) + [palabra[-1]])
    palabra = apostrofe_guion(palabra)
    return palabra
