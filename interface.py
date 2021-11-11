import tkinter

class Bienvenida():
    
    def __init__(self):

        #---------crea la raíz-------------
        self.raiz = tkinter.Tk()
        self.raiz.title("Encuesta")
        self.raiz.config(bg="light pink")
        self.raiz.geometry("1300x700")
        
        #----------crea el frame----------------  
        self.frame1 = tkinter.Frame(self.raiz, width=1000, height=500, bg="light blue")
        self.frame1.pack()
        
        #------------Crea un label que da la bienvenida al usuario
        bienvenida = tkinter.Label(self.frame1, text= "¡Sea usted bienvenida(o)! \n"
                              "El propósito de esta encuesta es generar una predicción de su voto en las "
                              "elecciones a la presidencia \n del próximo año, 2022. A partir de sus respuestas, "
                              "se generará su perfil político, y con base en este se \n escogerá un posible candidato "
                              "por el cual usted votaría. \n Los candidatos tomados en cuenta para esta encuesta fueron:"
                              "\n Alejandro Gaviria, Gustavo Petro, Mauricio Cárdenas, Sergio Fajardo, \n Federico Gutierrez, Óscar Iván"
                              " Zuluaga, Francia Márquez, Juan Manuel Galán,\n Jorge Enrique Robledo y Dilian Francisca Toro. \n"
                              "\n En la encuesta, se presentarán una serie de preguntas con diferentes opciones, por favor escriba en su teclado la \n opción que prefiera y "
                              "luego de 'click' en el botón 'Siguiente'. \n  Recuerde solo usar minúsculas y, en la última diapositiva, oprimir el botón 'OK' \n "
                              "\n Esperamos que sea de su agrado la encuesta, y recuerde, esto solo es una \n"
                              "especulación respecto a una lista reducida de candidatos. \n ¡Gracias!", 
                              font = ("Times New Roman", 14))
        bienvenida.grid(padx=100, pady=20)
         
        #-----------------Le pide al usuario que introduzca su nombre y le da un espacio
        #-----------------para que lo haga
        frase = tkinter.Label(self.frame1, text= "¡Empecemos! Por favor, oprima el botón", font = ("Times New Roman", 14))
        frase.grid(padx = 200, pady= 10)
        
        boton= tkinter.Button(self.frame1, text="Siguiente", command=self.siguiente)
        boton.grid(padx = 20, pady= 10)
        
        self.raiz.mainloop()
        
     
     
    def siguiente(self):
        self.raiz.destroy()

        
        