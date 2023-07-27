import sys


#comprobacion de seguridad. Ejecutar solo si se reciben 2 argumentos reales
if len(sys.argv)==3:              #Espera 2 parametros, xq el 1ro es siempre el nombre del archivo
    frase=sys.argv[1]
    cantidad=int(sys.argv[2])

    for r in range(cantidad):
        print(frase)
else:
    print("che te equivocaste de cantidad de argumentos")
    