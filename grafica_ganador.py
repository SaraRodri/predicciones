from matplotlib import pyplot
"""Los archivos 'graficar_r1', 'grafica_r2', 'grafica_r3', 'grafica_r4' y 
'grafica_ganador' son bastante parecidos, por lo que solo está comentado 'graficar_r1', para
evitar ser repetitiva"""

frase = open("resultado.txt", 'r')

lista = []
ct = 0

f = frase.readlines()

for i in f:
    eme = f[ct].split("  ")
    lista.append(eme)
    ct += 1


encuestados = ["Alejandro Gaviria", "Gustavo Petro", "Mauricio Cárdenas", "Sergio Fajardo", 
              "Federico Gutierrez", "Óscar Iván Zuluaga", "Francia Márquez", "Juan Manuel Galán",
                              "Jorge Enrique Robledo", "Dilian Francisca Toro", "Voto en Blanco"]


colores = ["indigo", "black", "green", "magenta", "blue", "pink", "purple", "red", "#DD969C", "orange", "#B0E0E6"]

votos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 

for linea in lista:
    if linea == lista[0]:
        None
    else:
        leng = len(linea[4]) 
        leng -= 3
        estrin = linea[4][0:leng]

        if estrin in "Usted va a votar por Alejandro Gaviria":
            votos[0] += 1
            
        elif estrin in "Usted va a votar por Gustavo Petro":
           votos[1] += 1
           
        elif estrin in "Usted va a votar por Mauricio Cárdenas":
            votos[2] += 1
            
        elif estrin in "Usted va a votar por Sergio Fajardo":
            votos[3] += 1
            
        elif estrin in "Usted va a votar por Federico Gutierrez":
            votos[4] += 1
            
        elif estrin in "Usted va a votar por Óscar Iván Zuluaga":
            votos[5] += 1
            
        elif estrin in "Usted va a votar por Francia Márquez":
            votos[6] += 1
            
        elif estrin in "Usted va a votar por Juan Manuel Galán":
            votos[7] += 1
            
        elif estrin in "Usted va a votar por Jorge Enrique Robledo":
            votos[8] += 1
            
        elif estrin in "Usted va a votar por Dilian Francisca Toro":
            votos[9] += 1
            
        elif estrin in "Usted va a votar por el voto en blanco":
            votos[10] += 1
        



_,_, texto = pyplot.pie(votos, colors = colores, labels = encuestados, autopct='%1.1f%%') #crea el pastel
for i in texto:
    i.set_color("white")
    
pyplot.axis('equal') #le da forma al pastel
pyplot.title("¿Quién fue el candidato preferido?")


pyplot.show

