from matplotlib import pyplot


frase = open("resultado.txt", 'r') #lee el txt resultante de "modular.py"

lista = []
ct = 0
colores = ("blue", "orange", "black") #los colores de la gráfica

f = frase.readlines() #lee una a una las lineas de la gráfica

for i in f:
    eme = f[ct].split("  ") #cada linea es un elemento de la lista "f", esto separa cada respuesta como un elemento aparte
    lista.append(eme) #añade cada elemento por aparte a una nueva lista
    ct += 1

r1 = [0, 0, 0]
for linea in lista:
    if linea == lista[0]: #el primer item de lista es "\n", con esto se salta ese item
        None
    elif linea[0] == "a": #con un iterador, va sumando la frecuencia de cada respuesta 
        r1[0] += 1
        
    elif linea[0] == "b":
        r1[1] += 1
        
    elif linea[0] == "c":
        r1[2] += 1


pregunta1 = ("a", "b", "c") #los nombres de las diferentes "tajadas" del pastel

_,_, texto = pyplot.pie(r1, colors = colores, labels = pregunta1, autopct='%1.1f%%') #crea el pastel
for i in texto:
    i.set_color("white") #le pone color blanco al pastel
    
pyplot.axis('equal') #le da forma al pastel
pyplot.title("¿Con qué frecuencia aparecieron estas respuestas \n en la pregunta 1?") #le da título a la gráfica

pyplot.show