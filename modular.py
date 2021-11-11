import tkinter
import interface


class Pregunta:
    def __init__(self, text, elemento):
        #--------------crear la raíz----------------
        
        self.elemento = elemento
        self.raiz = tkinter.Tk()
        self.raiz.title(f"Pregunta {elemento + 1}")
        self.raiz.config(bg="light pink")
        self.raiz.geometry("1000x500")

        #-----------------crear el frame-------------
        
        self.frame = tkinter.Frame(self.raiz, width=1000, height=500, bg="light blue")
        self.frame.pack()
        
        #--------------- Labels y Entrys que tiene la raíz-------
        self.text = text
        self.pregunta = tkinter.Label(self.frame, text = self.text, font = ("Times New Roman", 14))
        self.pregunta.grid(padx=100, pady=20)
        
        self.respuesta = tkinter.Entry(self.frame)
        self.respuesta.config(justify="center")
        self.respuesta.grid(padx = 200, pady= 10) 
    
        self.boton = tkinter.Button(self.frame, text="Siguiente", command = self.siguiente) #crea un botón que ejecuta siguiente 
        self.boton.grid(padx = 20, pady= 10)
        
        
        self.raiz.mainloop()
        
    def destruir(self):
        self.raiz.destroy()
        
    def siguiente(self):
        "Verifica si la opción introducida en el entry es válida"
        self.r = self.respuesta.get()
        
        if self.elemento == 0:
            if self.r =="a" or self.r =="b" or self.r =="c":    
                self.destruir()
            else:
                 self.incorrecto()
                 
        if self.elemento == 1:
            if self.r == "a" or self.r== "b" or self.r == "c" or self.r == "d":
                self.destruir()
            else:
                 self.incorrecto()
        
        if self.elemento == 2:
            if self.r =="a" or self.r == "b" or self.r =="c" or self.r == "d":
                self.destruir()
                    
            else:
                self.incorrecto()
                
        if self.elemento == 3:
            if self.r =="a" or self.r=="b" or self.r == "c" or self.r == "d" or self.r=="e" or self.r == "f":
                self.destruir()
            else:
                self.incorrecto()
        
        
    def incorrecto(self):
        "opción inválida"
        message = tkinter.Label(self.frame, text= "Por favor, escoja una opción válida", 
                              font = ("Times New Roman", 14))
        message.grid(padx = 20, pady= 10)
        
        
def arbol (r1, r2, r3, r4):
    "Basándose en sus respuestas, predice por quién votará el encuestado"
    win = tkinter.Tk() #crea la raíz
    win.geometry("500x500")
    win.config(bg="light pink")
    win.title("Resultado")
    
    if r1 == "a":
        if r2 == "a":
            if r3 == "a":
                if r4 == "a": 
                    respuesta = "Usted va a votar por Federico Gutierrez"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Juan Manuel Galán"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Francia Márquez"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Francia Márquez"
                elif r4 == "e":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
            elif r3 == "b":
                if r4 == "a":
                    respuesta = "Usted va a votar por Federico Gutierrez"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Federico Gutierrez"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Sergio Fajardo"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Francia Márquez"
                elif r4 == "e":
                    respuesta = "Usted va a votar por Francia Márquez"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
            elif r3 == "c":
                if r4 == "a":
                    respuesta = "Usted va a votar por Mauricio Cárdenas"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Juan Manuel Galán"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Alejandro Gaviria"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Francia Márquez"
                elif r4 == "e":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
            elif r3 == "d":
                if r4 == "a":
                    respuesta = "Usted va a votar por Óscar Iván Zuluaga"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Óscar Iván Zuluaga"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Alejandro Gaviria"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "e":
                    respuesta = "Usted va a votar por Gustavo Petro"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
        elif r2 == "b":
            if r3 == "a":
                if r4 == "a":
                    respuesta = "Usted va a votar por Mauricio Cárdenas"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Federico Gutierrez"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Alejandro Gaviria"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "e":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
            elif r3 == "b":
                if r4 == "a":
                    respuesta = "Usted va a votar por Juan Manuel Galán"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Alejandro Gaviria"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Alejandro Gaviria"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Sergio Fajardo"
                elif r4 == "e":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
            elif r3 == "c":
                if r4 == "a":
                    respuesta = "Usted va a votar por Dilian Francisca Toro"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Dilian Francisca Toro"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Alejandro Gaviria"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Sergio Fajardo"
                elif r4 == "e":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
            elif r3 == "d":
                if r4 == "a":
                    respuesta = "Usted va a votar por Mauricio Cárdenas"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Juan Manuel Galán"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Alejandro Gaviria"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "e":
                    respuesta = "Usted va a votar por Gustavo Petro"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
        elif r2 == "c":
            if r3 == "a":
                if r4 == "a":
                    respuesta = "Usted va a votar por Óscar Iván Zuluaga"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Juan Manuel Galán"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Alejandro Gaviria"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "e":
                    respuesta = "Usted va a votar por Gustavo Petro"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
            elif r3 == "b":
                if r4 == "a":
                    respuesta = "Usted va a votar por Dilian Francisca Toro"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Alejandro Gaviria"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Alejandro Gaviria"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Sergio Fajardo"
                elif r4 == "e":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
            elif r3 == "c":
                if r4 == "a":
                    respuesta = "Usted va a votar por Mauricio Cárdenas"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Juan Manuel Galán"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Alejandro Gaviria"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "e":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
            elif r3 == "d":
                if r4 == "a":
                    respuesta = "Usted va a votar por Mauricio Cárdenas"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Mauricio Cárdenas"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Alejandro Gaviria"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Sergio Fajardo"
                elif r4 == "e":
                    respuesta = "Usted va a votar por Gustavo Petro"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
        elif r2 == "d":
            if r3 == "a":
                if r4 == "a":
                    respuesta = "Usted va a votar por Dilian Francisca Toro"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Juan Manuel Galán"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Sergio Fajardo"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Sergio Fajardo"
                elif r4 == "e":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
            elif r3 == "b":
                if r4 == "a":
                    respuesta = "Usted va a votar por Federico Gutierrez"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Alejandro Gaviria"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Sergio Fajardo"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Sergio Fajardo"
                elif r4 == "e":
                    respuesta = "Usted va a votar por Francia Márquez"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
            elif r3 == "c":
                if r4 == "a":
                    respuesta = "Usted va a votar por Federico Gutierrez"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Juan Manuel Galán"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Juan Manuel Galán"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Francia Márquez"
                elif r4 == "e":
                    respuesta = "Usted va a votar por Francia Márquez"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
            elif r3 == "d":
                if r4 == "a":
                    respuesta = "Usted va a votar por Óscar Iván Zuluaga"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Alejandro Gaviria"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Alejandro Gaviria"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Sergio Fajardo"
                elif r4 == "e":
                    respuesta = "Usted va a votar por Gustavo Petro"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
    elif r1 == "b":
        if r2 == "a":
            if r3 == "a":
                if r4 == "a":
                    respuesta = "Usted va a votar por Federico Gutierrez"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Federico Gutierrez"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Francia Márquez"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "e":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
            elif r3 == "b":
                if r4 == "a":
                    respuesta = "Usted va a votar por Federico Gutierrez"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Federico Gutierrez"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Francia Márquez"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Francia Márquez"
                elif r4 == "e":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
            elif r3 == "c":
                if r4 == "a":
                    respuesta = "Usted va a votar por Mauricio Cárdenas"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Juan Manuel Galán"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Francia Márquez"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "e":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
            elif r3 == "d":
                if r4 == "a":
                    respuesta = "Usted va a votar por Óscar Iván Zuluaga"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Óscar Iván Zuluaga"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Sergio Fajardo"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "e":
                    respuesta = "Usted va a votar por Gustavo Petro"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
        elif r2 == "b":
            if r3 == "a":
                if r4 == "a":
                    respuesta = "Usted va a votar por Federico Gutierrez"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Alejandro Gaviria"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Sergio Fajardo"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Sergio Fajardo"
                elif r4 == "e":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
            elif r3 == "b":
                if r4 == "a":
                    respuesta = "Usted va a votar por Juan Manuel Galán"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Alejandro Gaviria"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Sergio Fajardo"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Sergio Fajardo"
                elif r4 == "e":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
            elif r3 == "c":
                if r4 == "a":
                    respuesta = "Usted va a votar por Dilian Francisca Toro"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Alejandro Gaviria"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Sergio Fajardo"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "e":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
            elif r3 == "d":
                if r4 == "a":
                    respuesta = "Usted va a votar por Juan Manuel Galán"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Alejandro Gaviria"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Alejandro Gaviria"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "e":
                    respuesta = "Usted va a votar por Gustavo Petro"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
        elif r2 == "c":
            if r3 == "a":
                if r4 == "a":
                    respuesta = "Usted va a votar por Juan Manuel Galán"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Óscar Iván Zuluaga"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Alejandro Gaviria"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Sergio Fajardo"
                elif r4 == "e":
                    respuesta = "Usted va a votar por Gustavo Petro"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
            elif r3 == "b":
                if r4 == "a":
                    respuesta = "Usted va a votar por Juan Manuel Galán"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Alejandro Gaviria"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Alejandro Gaviria"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Sergio Fajardo"
                elif r4 == "e":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
            elif r3 == "c":
                if r4 == "a":
                    respuesta = "Usted va a votar por Juan Manuel Galán"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Mauricio Cárdenas"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Alejandro Gaviria"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "e":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
            elif r3 == "d":
                if r4 == "a":
                    respuesta = "Usted va a votar por Juan Manuel Galán"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Alejandro Gaviria"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Alejandro Gaviria"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "e":
                    respuesta = "Usted va a votar por Gustavo Petro"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
        elif r2 == "d":
            if r3 == "a":
                if r4 == "a":
                    respuesta = "Usted va a votar por Juan Manuel Galán"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Juan Manuel Galán"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Sergio Fajardo"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "e":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
            elif r3 == "b":
                if r4 == "a":
                    respuesta = "Usted va a votar por Federico Gutierrez"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Alejandro Gaviria"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Sergio Fajardo"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Sergio Fajardo"
                elif r4 == "e":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
            elif r3 == "c":
                if r4 == "a":
                    respuesta = "Usted va a votar por Juan Manuel Galán"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Juan Manuel Galán"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Alejandro Gaviria"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Francia Márquez"
                elif r4 ==  "e":
                    respuesta = "Usted va a votar por Francia Márquez"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
            elif r3 == "d":
                if r4 == "a":
                    respuesta = "Usted va a votar por Óscar Iván Zuluaga"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Óscar Iván Zuluaga"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Alejandro Gaviria"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Sergio Fajardo"
                elif r4 == "e":
                    respuesta = "Usted va a votar por Gustavo Petro"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
    elif r1 == "c":
        if r2 == "a":
            if r3 == "a":
                if r4 == "a":
                    respuesta = "Usted va a votar por Federico Gutierrez"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Federico Gutierrez"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Francia Márquez"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "e":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
            elif r3 == "b":
                if r4 == "a":
                    respuesta = "Usted va a votar por Federico Gutierrez"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Federico Gutierrez"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Francia Márquez"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Francia Márquez"
                elif r4 == "e":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
            elif r3 == "c":
                if r4 == "a":
                    respuesta = "Usted va a votar por Mauricio Cárdenas"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Juan Manuel Galán"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Francia Márquez"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "e":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
            elif r3 == "d":
                if r4 == "a":
                    erespuesta = "Usted va a votar por Óscar Iván Zuluaga"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Óscar Iván Zuluaga"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Sergio Fajardo"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "e":
                    respuesta = "Usted va a votar por Gustavo Petro"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
        elif r2 == "b":
            if r3 == "a":
                if r4 == "a":
                    respuesta = "Usted va a votar por Mauricio Cárdenas"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Federico Gutierrez"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Alejandro Gaviria"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "e":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
            elif r3 == "b":
                if r4 == "a":
                    respuesta = "Usted va a votar por Juan Manuel Galán"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Alejandro Gaviria"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Sergio Fajardo"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Sergio Fajardo"
                elif r4 == "e":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
            elif r3 == "c":
                if r4 == "a":
                    respuesta = "Usted va a votar por Dilian Francisca Toro"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Dilian Francisca Toro"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Alejandro Gaviria"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Sergio Fajardo"
                elif r4 == "e":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
            elif r3 == "d":
                if r4 == "a":
                    respuesta = "Usted va a votar por Mauricio Cárdenas"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Juan Manuel Galán"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Alejandro Gaviria"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "e":
                    respuesta = "Usted va a votar por Gustavo Petro"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
        elif r2 == "c":
            if r3 == "a":
                if r4 == "a":
                    respuesta = "Usted va a votar por Óscar Iván Zuluaga"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Juan Manuel Galán"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Alejandro Gaviria"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "e":
                    respuesta = "Usted va a votar por Gustavo Petro"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
            elif r3 == "b":
                if r4 == "a":
                    respuesta = "Usted va a votar por Dilian Francisca Toro"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Alejandro Gaviria"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Alejandro Gaviria"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "e":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
            elif r3 == "c":
                if r4 == "a":
                    respuesta = "Usted va a votar por Mauricio Cárdenas"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Juan Manuel Galán"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Alejandro Gaviria"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "e":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
            elif r3 == "d":
                if r4 == "a":
                    respuesta = "Usted va a votar por Mauricio Cárdenas"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Mauricio Cárdenas"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Alejandro Gaviria"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Sergio Fajardo"
                elif r4 == "e":
                    respuesta = "Usted va a votar por Gustavo Petro"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
        elif r2 == "d":
            if r3 == "a":
                if r4 == "a":
                    respuesta = "Usted va a votar por Dilian Francisca Toro"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Juan Manuel Galán"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Sergio Fajardo"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Sergio Fajardo"
                elif r4 == "e":
                    respuesta = "Usted va a votar por Jorge Enrique Robledo"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
            elif r3 == "b":
                if r4 == "a":
                    respuesta = "Usted va a votar por Federico Gutierrez"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Alejandro Gaviria"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Sergio Fajardo"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Sergio Fajardo"
                elif r4 == "e":
                    respuesta = "Usted va a votar por Francia Márquez"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
            elif r3 == "c":
                if r4 == "a":
                    respuesta = "Usted va a votar por Federico Gutierrez"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Juan Manuel Galán"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Juan Manuel Galán"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Francia Márquez"
                elif r4 == "e":
                    respuesta = "Usted va a votar por Francia Márquez"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
            elif r3 == "d":
                if r4 == "a":
                    respuesta = "Usted va a votar por Óscar Iván Zuluaga"
                elif r4 == "b":
                    respuesta = "Usted va a votar por Alejandro Gaviria"
                elif r4 == "c":
                    respuesta = "Usted va a votar por Alejandro Gaviria"
                elif r4 == "d":
                    respuesta = "Usted va a votar por Sergio Fajardo"
                elif r4 == "e":
                    respuesta = "Usted va a votar por Gustavo Petro"
                elif r4 == "f":
                    respuesta = "Usted va a votar por el voto en blanco"
                              
    e3 = tkinter.Label(win, text=respuesta, bg="light blue", fg="black", font=("Times New Roman", 14))    #en una nueva ventana, le informa al usuario por quién votará
    e3.pack(padx=100, pady=100, ipadx=100, ipady=100, fill=tkinter.X)
    boton2= tkinter.Button(win, text="OK", command=win.destroy)
    boton2.pack()
    win.mainloop()
    return respuesta
        
    
encuesta = interface.Bienvenida()

pregunta1 =  Pregunta( "¿Usted va a votar en estas elecciones?\n"
                                     "\n a) Sí \n b) No \n c) No lo sé aun", 0)
        
pregunta2 = pregunta2 = Pregunta("Su candidato preferido debe enfocarse en\n"
                         "\n a) El medio ambiente \n b) La seguridad \n"
                " c) La reactivación económica \n d) La eliminación de la corrupción", 1)
        
pregunta3 = Pregunta("Este candidato debe generar\n" 
          "\n a) Confianza \n b) Unión \n c) Cohesión \n d) Estabilidad económica ", 2)
        
pregunta4 = Pregunta("Se considera una persona de\n"
           "\n a) Derecha \n b) Centro-derecha \n c) Centro \n d) Centro-izquierda"
           " \n e) Izquierda \n f) Ninguna de las anteriores", 3)
        
variable = arbol(pregunta1.r, pregunta2.r, pregunta3.r, pregunta4.r)

f = open("resultado.txt", 'a') #escribe en un archivo de texto los resultados de la encuesta cada vez que se corre el programa.
lista = [pregunta1.r, pregunta2.r, pregunta3.r, pregunta4.r, variable]
f.write("\n")
for i in lista:
    f.write(i + " ")      
f.close()       
        
        
        
        
        
        

        
        
        
        