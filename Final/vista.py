from tkinter import (
    StringVar,
    CENTER,
    Label,
    Button,
    Entry,
    DoubleVar,
    ttk,
)


from modelo import Abmc

# declaración de todas las variables del programa:


class Ventana:
    """
        Al instanciarse un objeto de la clase Ventana, se crea un objeto de la clase abmc para poder acceder a sus metodos de instancia
        y se setea la configuracion basica de la ventana junto con todos sus botones, entrys y labels. Tambien se crea el Tkinter.
        """
    def __init__(self, window):        
        self.objeto_base = Abmc()
        self.principal = window
        self.principal.geometry("729x365")  # tamaño de ventana
        self.principal.resizable(width=False, height=False)
        self.principal.title("Calculadora de costos en transformadores")

        # declaracion de los entry para que el usuario cargue datos:

        var_ordenar_str = StringVar()
        id = StringVar()
        var_cobre = DoubleVar()
        var_aceite = DoubleVar()
        var_pintura = DoubleVar()
        var_ogp = DoubleVar()
        var_mo = DoubleVar()
        var_id_buscar = StringVar()
        var_id_borrar = StringVar()
        costo_fijo = 400
        valor_transformador = 3750
        margen = 0
        w = 14

        self.numero_transformador = Entry(self.principal, textvariable=id, width=w)
        self.numero_transformador.grid(row=1, column=1)

        self.cobre = Entry(self.principal, textvariable=var_cobre, width=w)
        self.cobre.grid(row=2, column=1)

        self.aceite = Entry(self.principal, textvariable=var_aceite, width=w)
        self.aceite.grid(row=3, column=1)

        self.pintura = Entry(self.principal, textvariable=var_pintura, width=w)
        self.pintura.grid(row=4, column=1)

        self.ogp = Entry(self.principal, textvariable=var_ogp, width=w)
        self.ogp.grid(row=1, column=3)

        self.mo = Entry(self.principal, textvariable=var_mo, width=w)
        self.mo.grid(row=2, column=3)

        self.id_buscar = Entry(self.principal, textvariable=var_id_buscar, width=w)
        self.id_buscar.grid(row=1, column=6)

        self.id_borrar = Entry(self.principal, textvariable=var_id_borrar, width=w)
        self.id_borrar.grid(row=3, column=6)

        # declaración de los labels que le indican al usuario que datos ingresar:
        self.label_id = Label(self.principal, text="ID del Transformador: ")
        self.label_id.grid(row=1, column=0, sticky="W")

        self.label_cobre = Label(self.principal, text="Kg de cobre: ")
        self.label_cobre.grid(row=2, column=0, sticky="W")

        self.label_aceite = Label(self.principal, text="Lts de Aceite:")
        self.label_aceite.grid(row=3, column=0, sticky="W")

        self.label_pintura = Label(self.principal, text="Lts de Pintura:")
        self.label_pintura.grid(row=4, column=0, sticky="W")

        self.label_ogp = Label(self.principal, text="Precio de OGPs: ")
        self.label_ogp.grid(row=1, column=2, sticky="W")

        self.label_mo = Label(self.principal, text="Hs Mano de obra:")
        self.label_mo.grid(row=2, column=2, sticky="W")

        self.label_costo_fijo = Label(self.principal, text="Costo fijo promedio:")
        self.label_costo_fijo.grid(row=3, column=2, sticky="W")

        self.lavel_valor_costo_fijo = Label(
            self.principal, text=costo_fijo, borderwidth=3, relief="groove", width=12
        )
        self.lavel_valor_costo_fijo.grid(row=3, column=3, pady=3)

        self.ordenar_por = Label(self.principal, text="Ordenar por", width=12)
        self.ordenar_por.grid(row=4, column=3)

        self.var_ordenar = ttk.Combobox(
            self.principal, textvariable=var_ordenar_str, state="readonly"
        )
        self.var_ordenar.grid(column=3, row=5)
        self.var_ordenar["values"] = (
            "id",
            "cobre",
            "aceite",
            "pintura",
            "ogp",
            "margen",
        )
        self.var_ordenar.set("id")

        # definición de los botones de alta, modficar, buscar,borrar, sacar filtro y graficar:
        
        alta = Button(
            self.principal,
            text="alta",
            command=lambda: self.objeto_base.alta_trafo(
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
            ),
            width=10,
            background="lightgreen",
        )
        alta.grid(row=5, column=1, pady=3)
        
        modificar = Button(
            self.principal,
            text="modificar",
            command=lambda: self.objeto_base.modificar_trafo(
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
            ),
            width=10,
            background="#6CB7EB",
        )
        modificar.grid(row=5, column=2)
        
        buscar_por_id = Button(
            self.principal,
            text="Filtrar por ID",
            command=lambda: self.objeto_base.buscar_id(var_id_buscar, tree),
            width=10,
            background="yellow",
        )
        buscar_por_id.grid(row=1, column=5, padx=3, pady=3)
     
        borrar_por_id = Button(
            self.principal,
            text="Borrar ID",
            command=lambda: self.objeto_base.borrar_id(
                var_id_borrar, tree, var_ordenar_str
            ),
            background="red",
            width=10,
        )
        borrar_por_id.grid(row=3, column=5, padx=3, pady=1)
       
        quitar_filtros = Button(
            self.principal,
            text="Actualizar",
            command=lambda: self.objeto_base.mostrar(tree, var_ordenar_str),
            width=10,
            background="#F4F1CE",
        )
        quitar_filtros.grid(row=5, column=5)
       
        graficar = Button(
            self.principal,
            text="Grafico Margenes",
            command=lambda: self.objeto_base.graficos(),
            width=13,
            background="#E68849",
        )
        graficar.grid(row=5, column=0)
     
        # Hago el treeview

        tree = ttk.Treeview(self.principal)
        tree["columns"] = ("col1", "col2", "col3", "col4", "col5", "col6", "col7")

        tree.column("#0", width=90, anchor=CENTER)
        tree.column("col1", width=90, anchor=CENTER)
        tree.column("col2", width=90, anchor=CENTER)
        tree.column("col3", width=90, anchor=CENTER)
        tree.column("col4", width=90, anchor=CENTER)
        tree.column("col5", width=90, anchor=CENTER)
        tree.column("col6", width=90, anchor=CENTER)
        tree.column("col7", width=90, anchor=CENTER)

        tree.heading("#0", text="ID")
        tree.heading("col1", text="Cobre")
        tree.heading("col2", text="Pintura")
        tree.heading("col3", text="Aceite")
        tree.heading("col4", text="Mano de Obra")
        tree.heading("col5", text="OGP")
        tree.heading("col6", text="Costo fijo")
        tree.heading("col7", text="Margen")

        tree.grid(column=0, row=7, columnspan=7, padx=3)

        self.objeto_base.mostrar(tree, var_ordenar_str)
        # llamo a la funcion mostrar para que el programase inicie con la base de datos actualizada en el tree


# Nicolás Campanella Lerra
# Curso 999188622
# Python 3 - Nivel Intermedio
