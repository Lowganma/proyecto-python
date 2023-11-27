import pandas as pd
cantidad = []
productos = []
precio = [] 

def AgregarProducto(añadir_cantidad,añadir_producto,añadir_precio):         
    cantidad.append(añadir_cantidad)
    productos.append(añadir_producto)
    precio.append(añadir_precio)

def Buscar_producto(buscador): 
    posicion = productos.index(buscador)
    return (cantidad[posicion],productos[posicion], precio[posicion])

def Modificar_Producto(buscador,añadir_cantidad,añadir_producto,añadir_precio):
    posicion = productos.index(buscador)
    cantidad[posicion] = añadir_cantidad
    productos[posicion] = añadir_producto
    precio[posicion] = añadir_precio

def Mostrar_Producto():
    productos_info = []
    for i in range(len(productos)):
        producto = {
            "cantidad": cantidad[i],
            "nombre": productos[i],
            "precio": precio[i]
        }
        productos_info.append(producto)
    return productos_info

def Exportar_Excel():
    df = pd.DataFrame({
            "Cantidad": cantidad,
            "Producto": productos,
            "Precio $": precio
        })
    df.to_excel("inventario.xlsx", index=False)

def Borrar_Producto(buscador):
   
    if buscador in productos:
        posicion = productos.index(buscador)
        del cantidad[posicion]
        del productos[posicion]
        del precio[posicion]
        return (f"El producto {buscador} ha sido borrado exitosamente.")
    else:
        return (f"El producto {buscador} no se encuentra en la lista.")
