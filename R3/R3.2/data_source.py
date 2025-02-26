'''
Franco Chavez/Jordi Chuquimarca/Pol Cerrillo
2/05/2023
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
# Directorios de entrada y salida.
DIR_ENTRADA = os.path.join(".", "entrada")
DIR_SALIDA = os.path.join(".", "sortida")

def llegir_directori():
    arxius = os.listdir(DIR_ENTRADA)
    for arxiu in arxius:
        entrada_dir = os.path.join(DIR_ENTRADA, arxiu)
        if os.path.isfile(entrada_dir) and entrada_dir.endswith(".txt"):
            try:
                # Abre el archivo en modo lectura y lee todas las líneas.
                with open(entrada_dir, 'r', encoding='utf-8') as f:
                    linies = f.readlines()
                f.close()
                # Procesa cada línea del archivo utilizando una función de la librería 'crazy_words'.
                linies_boges = [crazy_words.leer_palabras(linia) + '\n' for linia in linies]
                escriptura_fitxers(linies_boges, arxiu)
            except Exception as e:
# Si hay un error durante la lectura o el procesamiento, registra el error utilizando una función definida en el módulo 'log'.
                log.error_log(e, entrada_dir)

def escriptura_fitxers(frase, arxiu):
    os.makedirs(DIR_SALIDA, exist_ok=True)
    output_file_path = os.path.join(DIR_SALIDA, arxiu + "_boges.txt")
    # Abre el archivo de salida en modo escritura y escribe las líneas procesadas.
    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.writelines(frase)
    f.close()

