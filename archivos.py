
def abrir(ruta):    
    archivo = open("{}".format(ruta),"r")
    return archivo.read()
    archivo.close()

def agregar(ruta,texto):
    archivo = open("{}".format(ruta),"w")
    archivo.write(texto)
    archivo.close()


def cerrar():
    pass

    
    