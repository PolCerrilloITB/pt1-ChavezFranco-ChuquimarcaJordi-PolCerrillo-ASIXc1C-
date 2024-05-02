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
import crazy_words
def get_data__from_keyboard():
    frase = str(input())
    return frase
def get_data_from_file(file_name):

def processar_paraules(arxiu_entrada, arxiu_sortida, arxiu_log):
    try:
        with open(arxiu_entrada, 'r') as f:
            paraules = f.read().split()
        processades = [palabra[::-1] for palabra in paraules]
        with open(arxiu_sortida, 'w') as f:
            for paraula in processades:
                f.write(paraula + '\n')
        with open(arxiu_log, 'a') as f:
            now = datetime.datetime.now()
            f.write(f"{now}: S'ha processat l'arxiu '{arxiu_entrada}'.\n")
    except Exception as e:
        with open(arxiu_log, 'a') as f:
            now = datetime.datetime.now()
            f.write(f"{now}: ERROR - {str(e)}\n")
processar_paraules(arxiu_entrada, arxiu_sortida, arxiu_log)

