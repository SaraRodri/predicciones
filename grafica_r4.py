from matplotlib import pyplot

frase = open("resultado.txt", 'r')

lista = []
ct = 0
colores = ("blue", "orange", "black", "pink", "green", "red")

f = frase.readlines()

for i in f:
    eme = f[ct].split("  ")
    lista.append(eme)
    ct += 1

r4 = [0, 0, 0, 0, 0, 0]
for linea in lista:
    if linea == lista[0]:
        None
    elif linea[3] == "a":
        r4[0] += 1
        
    elif linea[3] == "b":
        r4[1] += 1
        
    elif linea[3] == "c":
        r4[2] += 1

    elif linea[3] == "d":
        r4[3] +=1
        
    elif linea[3] == "e":
        r4[4] += 1
        
    elif linea [3] == "f":
        r4[5] += 1

pregunta4 = ("a", "b", "c", "d", "e", "f")

_,_, texto = pyplot.pie(r4, colors = colores, labels = pregunta4, autopct='%1.1f%%') #crea el pastel
for i in texto:
    i.set_color("white")
    
pyplot.axis('equal') #le da forma al pastel
pyplot.title("¿Con qué frecuencia aparecieron estas respuestas \n en la pregunta 4?") #le da título a la gráfica

pyplot.show