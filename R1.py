import  random
def desordenar_palabra(palabra):
        if len(palabra) <= 3:
            return palabra
        else:
            primera = palabra[0]
            ultima = palabra[-1]
            intermedio = list(palabra[1:-1])
            random.shuffle(intermedio)
            desorden = ''.join([primera] + intermedio + [ultima])
            return desorden
def desordenar_texto(frase):
    palabras = frase.split()
    mezcla = [desordenar_palabra(palabra) for palabra in palabras]
    frase_mezcla = ' '.join(mezcla)
    return frase_mezcla
def main():
    frase = str(input(" "))
    frase_mezcla = desordenar_texto(frase)
    print("", frase_mezcla)
main()