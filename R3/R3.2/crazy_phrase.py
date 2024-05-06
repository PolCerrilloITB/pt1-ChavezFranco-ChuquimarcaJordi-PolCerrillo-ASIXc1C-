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
#import crazy_words
#def frase_larga(palabra, frase):
 #   if palabra[-1] in crazy_words.caracteres and palabra[0] in crazy_words.caracteres:
#        signe_davant = palabra[0]
 #       signe_darrere = palabra[-1]
  #      palabra = palabra.replace(palabra[-1], "")
   #     palabra = palabra.replace(palabra[0], "")
    #    palabra = crazy_words.mezcla(palabra)
     #   palabra = signe_davant + palabra + signe_darrere
      #  frase = frase + palabra + " "
#    elif palabra[-1] in crazy_words.caracteres:
 #       signe_darrere = palabra[-1]
  #      palabra = palabra.replace(palabra[-1], "")
   #     palabra = crazy_words.mezcla(palabra)
    #    palabra = palabra + signe_darrere
     #   frase = frase + palabra + " "
#    elif palabra[0] in crazy_words.caracteres:
 #       signe_davant = palabra[0]
  #      palabra = palabra.replace(palabra[0], "")
   #     palabra = crazy_words.mezcla(palabra)
    #    palabra = signe_davant + palabra
     #   frase = frase + palabra + " "
#    else:
 #       palabra = crazy_words.mezcla(palabra)
  #      frase = frase + palabra + " "
   # return frase