import random
palabra = input().split()
palabra = str(palabra)
try:
    if len(palabra) <= 3:
        print("Demasiado corta")
    else:
        primera = palara[0]
        ultima = palanra[-1]
        intermedio = list(palabra[1:0])
        random.shuffle(intermedio)
        desorden = ''.join(primera + intermedio + ultima)
        #return desorden
except:
    print("")