# predicciones
Este es el repositorio del proyecto.

Contiene los archivos:

“preguntas”, que contiene las preguntas en su forma más básica, este
archivo se encarga de que el encuestado ingrese una opción válida y, en dado caso que
no sea así, le informa que su opción no es válida y le vuelve a arrojar la pregunta con
sus opciones.

“respuestas”, que contiene las 288 respuestas que puede llegar a obtener el
encuestado a raíz de evaluar su perfil político y seguir el árbol de decisiones ya
propuesto anteriormente.

“interface”, el primer archivo que contiene una interfaz. Da la bienvenida
al usuario, le pide su nombre y luego lo guía hacia la pregunta 1.

“pregunta1”, “pregunta2”, “pregunta3” y “pregunta4”, que contienen las
preguntas y una interfaz amigable para que el usuario pueda interactuar con ella. Los
archivos están conectados entre sí, y al dar click en el botón “siguiente” de un
archivo, la ventana del siguiente aparece en pantalla. Aún falta pulir que, al abrir una
ventana, la anterior se cierre.
En el archivo “pregunta4”, además, está incorporado el árbol de decisiones (cuyo
programa base se puede ver en el archivo “respuestas”) y está modificado de forma tal
en que funcione con la librería tkinter. A ese respecto, solo falta importar las variables
r1, r2 y r3 que se encuentran en los otros tres archivos y con ellas se terminaría el
árbol de decisiones.
