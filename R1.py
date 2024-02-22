import  random
def pedir_texto(palabra):
    try:
        if len(palabra) <= 3:
            return palabra
        else:
    except:
        print("La plabra ")

def desordenar_frase(frase):
    texto = texto.split()
    palabras_desordenadas = [desordenar_palabra(palabra) for palabra in texto]
    frase_desordenada = ' '.join(palabras_desordenadas)
    return frase_desordenada


def main():
    frase_original = input("Introduce una frase: ")
    frase_modificada = desordenar_frase
    print("Frase desordenada:", frase_modificada)
