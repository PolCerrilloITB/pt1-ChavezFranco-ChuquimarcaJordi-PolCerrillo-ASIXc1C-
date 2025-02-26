'''
Franco Chavez/Jordi Chuquimarca/Pol Cerrillo
02/05/2023
ASIXc1C M03 UF2
Descripción: Partint del problema general cal dividir-lo en problemes més simples, denominats subproblemes.
Així trobarem les funcions en les quals cal descompondre.
Un punt important, a tenir en compte en aplicar aquesta descomposició, és que cadascun dels subproblemes
no es genera arbitràriament, sinó que es planteja com un objectiu parcial, amb entitat pròpia, per resoldre
el seu problema de nivell superior. Un cop assolits tots aquests objectius parcials, es considera resolt el total.
'''
import data_source
import time
import log

def main():
    cont_s = time.time()
    log.info_log()
    data_source.get_data_from_file()
    print("El archivo se ha procesado")
    cont_f = time.time()
    duracion = cont_f - cont_s
    log.final_log(duracion)
main()
