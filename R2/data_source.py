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
import requests
API_KEY = 'MjOTkzw75nU7momSX5KDbQ==gVWI97BI0oLZ8eHj'
frase = "."
def get_data__from_keyboard():
    frase = str(input())
    return frase

def get_data_from_server(frase):
    frase = input()
    frase = requests.get(frase, headers={'X-Api-Key': API_KEY})
    if frase.status_code == 200:
        return frase.text
    else:
        print(f"Error al obtener el input desde la API. Código de estado: {frase.status_code}")
        return None

