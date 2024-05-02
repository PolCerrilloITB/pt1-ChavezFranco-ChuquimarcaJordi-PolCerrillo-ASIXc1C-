from crazy_words import frase, desordenar_palabra
def desordenar_frase(frase):
    palabras = frase.split()
    mezcla = [desordenar_palabra(palabra) for palabra in palabras]
    return ' '.join(mezcla)
