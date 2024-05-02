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
import datetime
import random
import re
import os
import crazy_words

def get_data_from_file():
    with open('entrada, paraules.txt', 'r') as f:
        paraules = f.read().split()
    paraules_desordenades = set()
    for paraula in paraules:
        paraula_desordenada = crazy_words.desordenar_palabra(paraula)
        paraules_desordenades.add(paraula_desordenada)
    return paraules_desordenades
def processar_paraules(paraules_desordenades):
    with open('sortida, paraules_boges.txt', 'w') as f:
        f.write(' '.join(paraules_desordenades))
        f.write('\n')
def escritura_arxiu_log(arxiu_entrada):
    try:
        with open('logs, boges.log', 'a') as f:
            now = datetime.datetime.now()
            f.write(f"{now}: S'han processat les paraules de l'arxiu '{arxiu_entrada}'.\n")
    except Exception as e:
        with open('boges.log', 'a') as f:
            now = datetime.datetime.now()
            f.write(f"{now}: ERROR - {str(e)}\n")




