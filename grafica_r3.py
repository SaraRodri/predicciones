from matplotlib import pyplot

frase = open("resultado.txt", 'r')

lista = []
ct = 0
colores = ("blue", "orange", "black", "pink")

f = frase.readlines()

for i in f:
    eme = f[ct].split("  ")
    lista.append(eme)
    ct += 1

r3 = [0, 0, 0, 0]
for linea in lista:
    if linea == lista[0]:
        None
    elif linea[2] == "a":
        r3[0] += 1
        
    elif linea[2] == "b":
        r3[1] += 1
        
    elif linea[2] == "c":
        r3[2] += 1
    
    elif linea[2] == "d":
        r3[3] +=1


pregunta3 = ("a", "b", "c", "d")

_,_, texto = pyplot.pie(r3, colors = colores, labels = pregunta3, autopct='%1.1f%%') #crea el pastel
for i in texto:
    i.set_color("white")
    
pyplot.axis('equal') #le da forma al pastel
pyplot.title("¿Con qué frecuencia aparecieron estas respuestas \n en la pregunta 3?") #le da título a la gráfica

pyplot.show