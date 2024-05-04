from crazy_words import caracteres, mezcla
def frase_larga(palabra, frase):
    if palabra[-1] in caracteres and palabra[0] in caracteres:
        signe_davant = palabra[0]
        signe_darrere = palabra[-1]
        palabra = palabra.replace(palabra[-1], "")
        palabra = palabra.replace(palabra[0], "")
        palabra = mezcla(palabra)
        palabra = signe_davant + palabra + signe_darrere
        frase = frase + palabra + " "
    elif palabra[-1] in caracteres:
        signe_darrere = palabra[-1]
        palabra = palabra.replace(palabra[-1], "")
        palabra = mezcla(palabra)
        palabra = palabra + signe_darrere
        frase = frase + palabra + " "
    elif palabra[0] in caracteres:
        signe_davant = palabra[0]
        palabra = palabra.replace(palabra[0], "")
        palabra = mezcla(palabra)
        palabra = signe_davant + palabra
        frase = frase + palabra + " "
    else:
        palabra = mezcla(palabra)
        frase = frase + palabra + " "
    return frase
