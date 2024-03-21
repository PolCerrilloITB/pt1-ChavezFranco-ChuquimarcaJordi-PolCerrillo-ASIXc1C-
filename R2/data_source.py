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
import openai
openai.api_key = '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'
API_KEY = 'MjOTkzw75nU7momSX5KDbQ==gVWI97BI0oLZ8eHj'


def get_data__from_keyboard(frase):
    frase = str(input())
    return frase


def get_data_from_server(frase):
    frase = str(input())
    frase = requests.get(frase, headers={'X-Api-Key': API_KEY})
    if frase.status_code == 200:
        return frase
    else:
        print(f"Error al obtener el input desde la API. Código de estado: {frase.status_code}")
        return None


def get_data_from_chatgpt(question):

    frase = openai.Completion.create(
        engine="text-davinci-002",
        prompt=question,
        max_tokens=200
    )
    return frase.choices[0].text.strip()


def get_data_from_file(file_name):
    pass

get_data__from_keyboard()