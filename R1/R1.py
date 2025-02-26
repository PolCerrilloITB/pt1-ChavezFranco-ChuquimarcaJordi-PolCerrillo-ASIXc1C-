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
import re
numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
def desordenar_palabra(palabra):
    if len(palabra) > 2:
        simbolos_principio = ''
        simbolos_final = ''
        if palabra[0] in ',.?¿¡!;:€@/()=&%$#"|':
            simbolos_principio = palabra[0]
            palabra = palabra[0:]
        if palabra[-1] in ',.?¿¡!;:€@/()=&%$#"|':
            simbolos_final = palabra[-1]
            palabra = palabra[:-1]
        apostrofe = -1
        if "'" in palabra:
            apostrofe = palabra.index("'")
            palabra = palabra.replace("'", "")
        intermedio = list(palabra[1:-1])
        random.shuffle(intermedio)
        if apostrofe != -1:
            intermedio.insert = (apostrofe.index - 1, "'")
        desordenar_palabra = simbolos_principio + palabra[0] + ''.join(intermedio) + palabra[-1] + simbolos_final
        url = None
        url_coinicde = re.search(r'(https://\s+)', palabra)
        if url_coinicde:
            url = url_coinicde.group(1)
            palabra = palabra.replace(url, "")
        return desordenar_palabra
    else:
        return palabra
def desordenar_texto(frase):
    palabras = frase.split()
    mezcla = [desordenar_palabra(palabra) for palabra in palabras]
    return ' '.join(mezcla)
def main():
    frase = str(input(""))
    frase_mezcla = desordenar_texto(frase)
    print(frase_mezcla)
main()