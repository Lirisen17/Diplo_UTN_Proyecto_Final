from tkinter import (
    messagebox,
    TclError,
)

# import sqlite3
from sqlite3 import connect, IntegrityError
from pandas import read_sql_query
from matplotlib.pyplot import bar, gca, title, show
from regex import validar
from peewee import *
from database import db,Transformador

from decoradores import decorador_alta,decorador_modificar,decorador_eliminar


costo_fijo = 400
valor_transformador = 3750
precio_cobre = 16
precio_pintura = 10
precio_aceite = 2
precio_mo = 2



db.connect()
db.create_tables([Transformador])

class Abmc:   
    
  

    def alta_trafo(
        self,
        var_ordenar_str,
        var_aceite,
        var_cobre,
        id,
        var_mo,
        var_ogp,
        var_pintura,
        valor_transformador,
        costo_fijo,
        margen,
        tree,
    ):
        """
        Este metodo toma los valores de los entry y los guarda en la base de datos.

        Args:
            :self (Abmc): Instancia de la clase Abmc
            :var_ordenar_str (StringVar): Da el orden para el treview. 
            :var_aceite (DoubleVar): Valor ingresado en el entry de los Lts de Aceite.
            :var_cobre (DoubleVar): Valor ingresado en el entry de los Kgs de Cobre.
            :id(StringVar): Valor ingresado Id del transformador. 
            :var_mo (DoubleVar): Valor ingresado en el entry de las horas hombre.
            :var_ogp (DoubleVar): Valor ingresado en el entry de los Otros Gastos de Produccion.
            :var_pintura (DoubleVar): Valor ingresado en el entry de los Lts de Pintura.
            :valor_transformador (int): Valor a cobrar de cada transformador.
            :costo_fijo(int): valor fijo del costo fijo que se le asigna a cada transformador.
            :margen (int): Variable inicializada en 0 que contendra el margen de cada transformador.
            :tree (Treeview): Variable del treeview.

        """
        trafo = Transformador()
        try:
            valor = str(id.get())            
            if validar(valor):                
                margen = (
                    float(valor_transformador)
                    - float(var_aceite.get() * precio_aceite)
                    - float(var_cobre.get() * precio_cobre)
                    - float(var_mo.get() * precio_mo)
                    - float(var_pintura.get() * precio_pintura)
                    - float(costo_fijo)
                    - float(var_ogp.get())
                )  
                
                trafo.mi_id = (int(id.get()))
                trafo.cobre = round(float(var_cobre.get() * precio_cobre), 2)
                trafo.pintura = round(float(var_pintura.get() * precio_pintura), 2)
                trafo.aceite = round(float(var_aceite.get() * precio_aceite), 2)
                trafo.mo = round(float(var_mo.get() * precio_mo), 2)
                trafo.ogp = round(float(var_ogp.get()), 2)
                trafo.costos_fijos = costo_fijo
                trafo.valor_transformador = valor_transformador
                trafo.margen = round(float(margen), 2)
                trafo.save()
                
                self.mostrar(tree, var_ordenar_str)
                self.alta_correcta()
            else:

                messagebox.showinfo(
                    message="El campo id solo admite números", title="Error"
                )
        except TclError:
            messagebox.showinfo(
                message="Valores invalidos. Recuerda que solo se admiten numeros reales!",
                title="Error",
            )
        except IntegrityError:
            messagebox.showinfo(message="Este transformador ya existe!", title="Error")
    

    #funcion usada para mostrar que el objeto se dio de alta correctamente y usar el decorador que muestre el alta por consola

    
    @decorador_alta
    def alta_correcta(self):
        messagebox.showinfo(
                    message="Transformador registrado correctamente!", title="Mensaje"
                ) 
    

    def modificar_trafo(
        self,
        var_ordenar_str,
        tree,
        var_aceite,
        var_cobre,
        id,
        var_mo,
        var_ogp,
        var_pintura,
        valor_transformador,
        costo_fijo,
        margen,
    ):
        """
        Este metodo toma los valores de los entry y los reemplaza en la base de datos en el registro que coincida con la id.

        Args:
            :self (Abmc): Instancia de la clase Abmc
            :var_ordenar_str (StringVar): Da el orden para el treview. 
            :var_aceite (DoubleVar): Valor ingresado en el entry de los Lts de Aceite.
            :var_cobre (DoubleVar): Valor ingresado en el entry de los Kgs de Cobre.
            :id (StringVar): Valor ingresado Id del transformador. 
            :var_mo (DoubleVar): Valor ingresado en el entry de las horas hombre.
            :var_ogp (DoubleVar): Valor ingresado en el entry de los Otros Gastos de Produccion.
            :var_pintura (DoubleVar): Valor ingresado en el entry de los Lts de Pintura.
            :valor_transformador (int): Valor a cobrar de cada transformador.
            :costo_fijo(int): Valor fijo del costo fijo que se le asigna a cada transformador.
            :margen (int): Variable inicializada en 0 que contendra el margen de cada transformador.
            :tree (Treeview): Variable del treeview.

        """
        try:  
            valor = str(id.get())            
            if validar( valor):               
                margen = (
                    float(valor_transformador)
                    - float(var_aceite.get() * precio_aceite)
                    - float(var_cobre.get() * precio_cobre)
                    - float(var_mo.get() * precio_mo)
                    - float(var_pintura.get() * precio_pintura)
                    - float(costo_fijo)
                    - float(var_ogp.get())
                )  # Calculo el margen restandoselo el valor del transformador a todos los costos
                
                cobre_var = round(float(var_cobre.get() * precio_cobre), 2)
                pintura_var = round(float(var_pintura.get() * precio_pintura), 2)
                aceite_var = round(float(var_aceite.get() * precio_aceite), 2)
                mo_var = round(float(var_mo.get() * precio_mo), 2)
                ogp_var = var_ogp.get()               
                margen_var = round(float(margen), 2)          
                actualizar = Transformador.update(cobre= cobre_var,pintura= pintura_var, aceite= aceite_var, mo= mo_var, ogp= ogp_var, margen = margen_var).where(Transformador.mi_id == valor)
                actualizar.execute()
                
                self.mostrar(tree, var_ordenar_str)
            else:
                messagebox.showinfo(
                    message="El campo id solo admite números", title="Error"
                )
        except TclError:
            messagebox.showinfo(
                message="Valores invalidos. Recuerda que solo se admiten numeros reales!",
                title="Error",
            )
        else:  
            self.mod_correcta()
    
    @decorador_modificar
    def mod_correcta(self):
        messagebox.showinfo(
                    message="Transformador modificado correctamente!", title="Mensaje"
                ) 
   
    def buscar_id(self, var_id_buscar, tree):
        """
        Este metodo busca una registro en la base de dato por la id.

        Args:
            :self (Abmc): Instancia de la clase Abmc.
            :var_id_buscar (StringVar): Variable que contiene la id a buscar
            :tree (Treeview): Variable del treeview.

        """
        valor = str(var_id_buscar.get())       
        if validar(valor):           
            mi_id = int(var_id_buscar.get())
            resultado = Transformador.select().where(Transformador.mi_id == mi_id)
            tree.delete(*tree.get_children())
            
            for i in resultado:
                tree.insert(  
                    "",
                    "end",
                    text=i.mi_id,
                    values=(
                        i.cobre,
                        i.pintura,
                        i.aceite,
                        i.mo,
                        i.ogp,
                        i.costos_fijos,
                        i.margen,
                    ),
                )
        else:
            messagebox.showinfo(
                message="El campo id solo admite números", title="Error"
            )
    
    def borrar_id(self, var_id_borrar, tree, var_ordenar_str):
        """
        Este metodo busca una registro en la base de dato por la id y lo borra.

        Args:
            :self (Abmc): Instancia de la clase Abmc.
            :var_id_borrar (StringVar): Variable que contiene la id a buscar
            :tree (Treeview): Variable del treeview.
            :var_ordenar_str (StringVar): Da el orden para el treview.
        """
        valor = str(var_id_borrar.get())        
        if validar(valor):  # uso regex para validar el ingreso de id
            try:
                mi_id = int(var_id_borrar.get())
                contrador_inicial = self.contador_registros()
                borrar = Transformador.get(Transformador.mi_id== mi_id)
                borrar.delete_instance()                
                self.mostrar(tree, var_ordenar_str)
                contador_final = self.contador_registros()
                if (
                    contrador_inicial != contador_final
                ):  
                    self.eliminar_correcto()
            except:
                 messagebox.showinfo(message="El registro ingresado no existe.", title="Error")
                                 
        else:
            messagebox.showinfo(message="El campo solo admite números.", title="Error")
    

    @decorador_eliminar
    def eliminar_correcto(self):
        messagebox.showinfo(
                    message="Registro Eliminado!", title="Mensaje"
                ) 
        
    def mostrar(self, tree, var_ordenar_str):
        """
        Este metodo inserta todos los registros de la base en el treeview ordenados segun la opcion elegida en el combobox.

        Args:
            :self (Abmc): Instancia de la clase Abmc.
            :var_ordenar_str (StringVar): Da el orden para el treview segun lo que eligio el usuario en el combobox.
            :tree (Treeview): Variable del treeview.
        """

        aux = str(var_ordenar_str.get())
        if aux == "":  
            aux = "id"      
        tree.delete(*tree.get_children())
        
        if aux == "cobre":
            ordenado = Transformador.cobre
        elif aux == "aceite":
            ordenado = Transformador.aceite
        elif aux == "ogp":
            ordenado = Transformador.ogp
        elif aux == "pintura":
            ordenado = Transformador.pintura
        elif aux == "margen":
            ordenado = Transformador.margen
        else:
            ordenado = Transformador.mi_id
        for i in Transformador.select().order_by(ordenado):  
            tree.insert(  
                "",
                "end",
                text=i.mi_id,
                values=(
                    i.cobre,
                    i.pintura,
                    i.aceite,
                    i.mo,
                    i.ogp,
                    i.costos_fijos,
                    i.margen,
                ),
            )
    
   
    def contador_registros(self):
        """
        Este metodo cuenta los registros existentes en la base de datos.

        Args:
            :self (Abmc): Instancia de la clase Abmc

        :returns: La cantidad de registros de la base de datos.
        """
        sql = Transformador.select()        
        return len(sql)
    
    
    def graficos(self):
        """
        Este metodo muestra un grafico en pantalla del margen de cada transformador. 
        Usa pandas para crear un dataframe y lo grafica mediante matplotlib.

        Args:
            :self (Abmc): Instancia de la clase Abmc.

        """        
        con = connect("base_trafos1.db")        
        try:
            df = read_sql_query(
                    "SELECT mi_id, margen from Transformador", con, index_col="mi_id"
                )

            df["margen"].plot(kind="bar")

            bar(
                    range(self.contador_registros()),
                    df["margen"],
                    align="center",
                    color=["blue", "red", "lightgreen", "orange", "yellow", "purple"],
                    edgecolor="black",
                )
            ax = gca()
            ax.set_facecolor("lightgrey")
            ax.set_ylabel("Margen")
            title("Margen de ganancia de cada transformador")
            show()
        except:
            messagebox.showinfo(
                message="La base de datos esta vacia. No hay graficos para mostrar.",
                title="Error",
             )


# Nicolás Campanella Lerra
# Curso 999188622
# Python 3 - Nivel Intermedio