import pandas as pd
cantidad = []
productos = []
precio = [] 

def AgregarProducto():
    añadir_cantidad = int(input("Ingrese la cantidad de su producto: "))
    añadir_producto = input("Ingrese el nombre de su producto: ")
    añadir_precio = float(input("Ingrese el precio de su producto: "))
                
    cantidad.append(añadir_cantidad)
    productos.append(añadir_producto)
    precio.append(añadir_precio)

def Buscar_producto(): 
    buscador = input("Ingrese el nombre del producto que quiere buscar: ")
    posicion = productos.index(buscador)
    return (cantidad[posicion],productos[posicion], precio[posicion])

def Modificar_Producto():
    buscador = input("Ingrese el nombre del producto que quiere modificar: ")
    posicion = productos.index(buscador)
    añadir_cantidad = int(input("Ingrese la cantidad de su producto: "))
    añadir_producto = input("Ingrese el nombre de su producto: ")
    añadir_precio = float(input("Ingrese el precio de su producto: "))

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

def Borrar_Producto():
    buscador = input("Ingrese el nombre del producto que quiere borrar: ")
    if buscador in productos:
        posicion = productos.index(buscador)
        del cantidad[posicion]
        del productos[posicion]
        del precio[posicion]
        print(f"El producto {buscador} ha sido borrado exitosamente.")
    else:
        print(f"El producto {buscador} no se encuentra en la lista.")