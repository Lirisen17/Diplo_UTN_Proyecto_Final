from tkinter import Tk
from vista import Ventana

def controlador(): #funcion creada solo para poder agregar el comentario a la documentacion de Sphinx
    """
    Archivo controlador del patron MVC. Crea la variable del Tkinter y crea una instancia de la clase Ventana de la vista.
    """
    pass


if __name__ == "__main__":    
    main = Tk()
    aplicacion = Ventana(main)
    main.mainloop()


# Nicolás Campanella Lerra
# Curso 999188622
# Python 3 - Nivel Intermedio

