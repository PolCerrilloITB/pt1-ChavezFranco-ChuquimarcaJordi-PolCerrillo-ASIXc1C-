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
numeros = ["0" "1" "2" "3" "4" "5" "6" "7" "8" "9"]
import random
import re
def desordenar_frase(frase):
    palabras = frase.split()
    mezcla = [desordenar_palabra(palabra) for palabra in palabras]
    frase_mezcla = ' '.join(mezcla)
    return frase_mezcla
def desordenar_palabra(frase):
    if len(frase) > 2:
        simbolos_principio = ''
        simbolos_final = ''
        if frase in numeros:
            frase = frase
        if frase[0] in ',.?¿¡!;:€@/()=&%$#"|':
            simbolos_principio = frase[0]
            frase = frase[0:]
        if frase[-1] in ',.?¿¡!;:€@/()=&%$#"|':
            simbolos_final = frase[-1]
            frase = frase[:-1]
        apostrofe = -1
        if "'" in frase:
            apostrofe = frase.index("'")
            frase = frase.replace("'", "")
        intermedio = list(frase[1:-1])
        random.shuffle(intermedio)
        if apostrofe != -1:
            intermedio.insert =(apostrofe.index - 1, "'")
            mezcla = simbolos_principio + frase[0] + ''.join(intermedio) + frase[-1] + simbolos_final
        url = None
        url_coinicde = re.search(r'(https://\s+)', frase)
        if url_coinicde:
            url = url_coinicde.group(1)
            frase = frase.replace(url, "")
        return desordenar_palabra
    else:
        return frase
def printar_pedir_frase():
    frase = str(input(""))
    frase_mezcla = desordenar_texto(frase)
    print(frase_mezcla)
    return printar_frase_final
