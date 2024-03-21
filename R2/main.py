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
    print(1,"Get data from keyboard")
    print(2, "Get data from server")
    print(3, "Get data from chatGPT")
    print(4, "Get data from file")
    choise = input()
    if choise == "1":
        eleccion = data_source.get_data__from_keyboard()
    elif choise == "2":
        eleccion = data_source.get_data_from_server()
    elif choise == "3":
        pregunta = input("Cual es tu pregunta?")
        eleccion = data_source.get_data_from_chatgpt(pregunta)
    elif choise == "4":
        print("Proximament")
    else:
        print("Escoje una de las siguientes opciones")
    if choise in ["1", "2", "3", "4"]:
        desordenar_palabra = crazy_words.printar_pedir_frase(eleccion)
        print(desordenar_palabra)
main()