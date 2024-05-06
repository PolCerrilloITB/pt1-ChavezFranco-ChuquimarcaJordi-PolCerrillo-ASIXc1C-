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
import os
import crazy_words
import log
DIR_ENTRADA = os.path.join(".", "entrada")
DIR_SALIDA = os.path.join(".", "sortida")

def get_data_from_file():
    arxius = os.listdir(DIR_ENTRADA)
    for arxiu in arxius:
        entrada_dir = os.path.join(DIR_ENTRADA, arxiu)
        if os.path.isfile(entrada_dir) and entrada_dir.endswith(".txt"):
            try:
                with open(entrada_dir, 'r', encoding='utf-8') as f:
                    linies = f.readlines()
                f.close()
                linies_boges = [crazy_words.leer_palabras(linia) + '\n' for linia in linies]
                escriptura_fitxers(linies_boges, arxiu)
            except Exception as e:
                log.error_log(e, entrada_dir)

def escriptura_fitxers(frase, arxiu):
    os.makedirs(DIR_SALIDA, exist_ok=True)
    output_file_path = os.path.join(DIR_SALIDA, arxiu + "_boges.txt")
    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.writelines(frase)
    f.close()


