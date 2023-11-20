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
                AgregarProducto()
            elif respuesta == 2:
                print(Buscar_producto())
            elif respuesta == 3:
                Modificar_Producto()
            elif respuesta == 4:
                print(Mostrar_Producto())
            elif respuesta == 5:
                Borrar_Producto()
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
