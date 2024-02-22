import  random
def desordenar_palabra(palabra):
        if len(palabra) > 2:
            puntuacion = ''
            if palabra[-1] in ',.?!;:':
                puntuacion = palabra[-1]
                palabra = palabra[:-1]
            intermedio = list(palabra[1:-1])
            random.shuffle(intermedio)
            desorden = palabra[0] + ''.join(intermedio) + palabra[-1] + puntuacion
            return desorden
        else:
            return palabra
def desordenar_texto(frase):
    palabras = frase.split()
    mezcla = [desordenar_palabra(palabra) for palabra in palabras]
    frase_mezcla = ' '.join(mezcla)
    return frase_mezcla
def main():
    frase = str(input(""))
    frase_mezcla = desordenar_texto(frase)
    print("", frase_mezcla)
main()