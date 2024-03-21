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
from openai import OpenAI
API_KEY = 'MjOTkzw75nU7momSX5KDbQ==gVWI97BI0oLZ8eHj'
def get_data__from_keyboard():
    frase = str(input())
    return frase
def get_data_from_server():
    api_url = 'https://api.api-ninjas.com/v1/randomword'
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    if response.status_code == requests.codes.ok:
        return response.text.replace('{', '').replace('"', '').replace('}', '')
    else:
        return "Error:" .format(response.status_code, response.text)
def get_data_from_chatgpt(question):
    api_key = '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'
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": question,
            }
        ],
    )
    generar_texto = response.choices[0].message.content
    return(generar_texto)
def get_data_from_file(file_name):
    pass

