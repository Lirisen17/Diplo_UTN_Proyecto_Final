def decorador_alta(funcion):
    def envoltura(*args, **kwargs):
        print("Ingreso de nuevo transformador correcto")
        return funcion(*args, **kwargs)
    return envoltura

def decorador_modificar(funcion):
    def envoltura(*args, **kwargs):
        print("Transformador modificado correctamente")
        return funcion(*args, **kwargs)
    return envoltura

def decorador_eliminar(funcion):
    def envoltura(*args, **kwargs):
        print("Transformador eliminado correctamente")
        return funcion(*args, **kwargs)
    return envoltura