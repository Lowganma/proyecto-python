from funciones import Modificar_Producto,AgregarProducto,Buscar_producto, Mostrar_Producto, Exportar_Excel, Borrar_Producto

print("Programa de gestion de inventarios".center(60,"-"))
def main():

    while True:
        try:
            print("""
            (1) Anadir productos
            (2) Buscar productos
            (3) Modificar productos
            (4) Ver productos
            (5) borrar producto 
            (6) guardar
            (7) salir      
            """)

            respuesta = int(input("Ingrese su opcion: "))
            if respuesta == 1:
                añadir_cantidad = int(input("Ingrese la cantidad de su producto: "))
                añadir_producto = input("Ingrese el nombre de su producto: ")
                añadir_precio = float(input("Ingrese el precio de su producto: "))
                AgregarProducto(añadir_cantidad,añadir_producto,añadir_precio)
            elif respuesta == 2:
                buscador = input("Ingrese el nombre del producto que quiere buscar: ")
                print(Buscar_producto(buscador))
            elif respuesta == 3:
                buscador = input("Ingrese el nombre del producto que quiere modificar: ")
                añadir_cantidad = int(input("Ingrese la cantidad de su producto: "))
                añadir_producto = input("Ingrese el nombre de su producto: ")
                añadir_precio = float(input("Ingrese el precio de su producto: "))
                Modificar_Producto(buscador,añadir_cantidad,añadir_producto,añadir_precio)
            elif respuesta == 4:
                print(Mostrar_Producto())
            elif respuesta == 5:
                buscador = input("Ingrese el nombre del producto que quiere borrar: ")
                print(Borrar_Producto(buscador))
            elif respuesta == 6:
                Exportar_Excel()
            else:
                break
        except ValueError:
            print("Por favor, ingrese un número válido.")        
        except Exception as e:
            print("Ocurrió un error:", e)    

if __name__ == "__main__":
    main()
