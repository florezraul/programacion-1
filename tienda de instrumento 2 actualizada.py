# Definir los productos disponibles
productos = {
     "1": {"nombre": "flauta", "tipo": "viento", "precio": 740000},
    "2": {"nombre": "clarinete", "tipo": "viento", "precio": 2000000},
    "3": {"nombre": "saxofón", "tipo": "viento", "precio": 1850000},
    "4": {"nombre": "batería", "tipo": "percusión", "precio": 1999999},
    "5": {"nombre": "congas", "tipo": "percusión", "precio": 275800},
    "6": {"nombre": "timbales", "tipo": "percusión", "precio": 690000},
    "7": {"nombre": "violín", "tipo": "cuerda", "precio": 350000},
    "8": {"nombre": "piano", "tipo": "cuerda", "precio": 5000000},
    "9": {"nombre": "guitarra", "tipo": "cuerda", "precio": 590000},
    "10": {"nombre": "ukulele", "tipo": "cuerda", "precio": 212900},
    "11": {"nombre": "acordeón", "tipo": "otros", "precio": 5700000},
    "12": {"nombre": "guitarra eléctrica", "tipo": "otros", "precio": 878000}
}

# Pedir los datos del comprador
nombre_comprador = input("Ingrese su nombre: ")
direccion_comprador = input("Ingrese su dirección: ")
cedula=int(input("Ingrese su número de cédula: "))
tel=int(input("Ingrese su número de teléfono: "))


# Mostrar los productos disponibles
print("Bienvenido/a a la tienda de instrumentos musicales!")
print("Estos son los productos disponibles:")

for nombre, datos in productos.items():
    print(nombre + " - " + datos["nombre"] + " - " + str(datos["precio"]))

# Pedir al usuario que seleccione los productos que quiere comprar
carrito = {}

while True:
    producto = input("Ingrese el nombre del producto que desea comprar (o 'salir' para finalizar la compra): ")
    if producto == "salir":
        break
    if producto not in productos:
        print("El producto ingresado no es válido.")
    else:
        cantidad = int(input("Ingrese la cantidad que desea comprar: "))
        carrito[producto] = cantidad
        print("Producto agregado al carrito.")

# Generar la factura
print("---------- FACTURA ----------")
print("Nombre del comprador: " + nombre_comprador)
print("Dirección del comprador: " + direccion_comprador)
print(f"Número de teléfono: ", {tel})
print(f"Su cédula es:", {cedula})
print("Productos comprados:")
total = 0
for nombre, cantidad in carrito.items():
    precio = productos[nombre]["precio"]
    subtotal = precio * cantidad
    print(nombre + " - " + str(precio) + " - " + str(cantidad) + " - " + str(subtotal))
    total += subtotal
print("Total de la compra: " + str(total))
print("------------------------------")

print("¡Gracias por su compra! Vuelva pronto.")


