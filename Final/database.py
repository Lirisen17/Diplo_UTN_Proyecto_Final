from peewee import *

db = SqliteDatabase("base_trafos1.db")

class BaseModel(Model):
    class Meta:
        database = db

class Transformador (BaseModel):
    """
    Esta Clase crea la estructura de la tabla transformadores
    
    
    """


    mi_id = IntegerField(unique=True)
    cobre = FloatField()
    pintura = FloatField()
    aceite = FloatField()
    mo =  FloatField()
    ogp = FloatField()
    costos_fijos = FloatField()
    valor_transformador = FloatField()
    margen = FloatField()


# Nicolás Campanella Lerra
# Curso 999188622
# Python 3 - Nivel Intermedio