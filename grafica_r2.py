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

r2 = [0, 0, 0, 0]
for linea in lista:
    if linea == lista[0]:
        None
    elif linea[1] == "a":
        r2[0] += 1
        
    elif linea[1] == "b":
        r2[1] += 1
        
    elif linea[1] == "c":
        r2[2] += 1
    
    elif linea[1] == "d":
        r2[3] +=1


pregunta2 = ("a", "b", "c", "d")

_,_, texto = pyplot.pie(r2, colors = colores, labels = pregunta2, autopct='%1.1f%%') #crea el pastel
for i in texto:
    i.set_color("white")
    
pyplot.axis('equal') #le da forma al pastel
pyplot.title("¿Con qué frecuencia aparecieron estas respuestas \n en la pregunta 2?") #le da título a la gráfica

pyplot.show