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
import crazy_words
import data_source
def main():
    frase = ""
    print(1,"Get data from keyboard")
    print(2, "Get data from server")
    print(3, "Get data from chatGPT")
    print(4, "Get data from file")
    eleccion = input()
    if eleccion == "1":
        frase = data_source.get_data__from_keyboard()
    elif eleccion == "2":
        frase = data_source.get_data_from_server()
    elif eleccion == "3":
        question = input("Cual es tu pregunta?")
        frase = data_source.get_data_from_chatgpt(question)
    elif eleccion == "4":
        print("Proximamente")
    else:
        print("Escoje una de las siguientes opciones")
    if eleccion in ["1", "2", "3", "4"]:
        desordenar_palabra = crazy_words.printar_pedir_frase(frase)
        print(desordenar_palabra)


main()