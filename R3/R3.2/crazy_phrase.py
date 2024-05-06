import crazy_words
def frase_larga(palabra, frase):
    if palabra[-1] in crazy_words.caracteres and palabra[0] in crazy_words.caracteres:
        signe_davant = palabra[0]
        signe_darrere = palabra[-1]
        palabra = palabra.replace(palabra[-1], "")
        palabra = palabra.replace(palabra[0], "")
        palabra = crazy_words.mezcla(palabra)
        palabra = signe_davant + palabra + signe_darrere
        frase = frase + palabra + " "
    elif palabra[-1] in crazy_words.caracteres:
        signe_darrere = palabra[-1]
        palabra = palabra.replace(palabra[-1], "")
        palabra = crazy_words.mezcla(palabra)
        palabra = palabra + signe_darrere
        frase = frase + palabra + " "
    elif palabra[0] in crazy_words.caracteres:
        signe_davant = palabra[0]
        palabra = palabra.replace(palabra[0], "")
        palabra = crazy_words.mezcla(palabra)
        palabra = signe_davant + palabra
        frase = frase + palabra + " "
    else:
        palabra = crazy_words.mezcla(palabra)
        frase = frase + palabra + " "
    return frase