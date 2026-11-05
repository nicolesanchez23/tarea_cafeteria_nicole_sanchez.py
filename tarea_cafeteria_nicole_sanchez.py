# ==========================================
# SISTEMA DE PEDIDOS PARA CAFETERÍA
# ==========================================

#Primero definimos el menú de opciones
#Permite asociar una clave (el nombre del producto en texto) con un valor (su precio en número decimal)
cafeteria_menu = {
    "café americano sencillo": 1.200,
    "cappuccino": 1.850,
    "frapucchino": 2.000,
    "croissant": 1.500,
    "pastel de frutos rojos": 1.000,
    "jugo de naranja": 850,
    "Crepa de fresas": 1.900
    }

#Creamos un diccionario para almacenar el pedido actual del cliente (producto: cantidad)
#Un diccionario vacío que comenzará sin ningún elemento. 
#A medida que el cliente elija productos, iremos guardando ahí el nombre del producto y la cantidad que pidió
pedido_actual = {}

# 2. Solicitar el nombre del cliente y mostrar un saludo personalizado
print("¡Bienvenidx a la Cafetería Arcoíris!")
nom_cliente = input("Por favor, ingresa tu nombre: ").strip()
print(f"\n¡Hola, {nom_cliente}! Es un gusto atenderte hoy :3\n")

# 3. Bucle principal del sistema que se repite hasta que el usuario decida salir
while True: #Crea un bucle que se repetirá indefinidamente hasta que el código ejecute un break.
    print("---* MENÚ DE OPCIONES *---")
    print("a. Ver el menú")
    print("b. Agregar un producto a tu pedido")
    print("c. Ver tu pedido actual")
    print("d. Finalizar el pedido y salir")
    
    opcion = input("Elige una opción (a/b/c/d): ").lower().strip()
    # el .lower convierte la entrada del usuario a minúsculas, y el .strip() elimina espacios en blanco al inicio y al final de la cadena.
    
    # 4. Validación de opción inexistente
    if opcion not in ['a', 'b', 'c', 'd']:
        print("\n[ERROR] Opción no válida. Por favor, selecciona una opción entre 'a', 'b', 'c' o 'd'.\n")
        continue  # Salta a la siguiente iteración del bucle while
    #La validación y continue: Si el usuario escribe una letra que no está permitida, el condicional if detecta el error, muestra un mensaje y utiliza continue. 
    #La sentencia continue hace que Python ignore lo que resta del bucle en ese turno y vuelva directamente al inicio a mostrar el menú de opciones otra vez.
    
    #Parte 5 opción A - Ver el Menú (Diccionarios y Enumerate) y opcion B - Agregar Producto (Bucle For/Else y Validaciones)
    
    # Opción A: Ver el menú de productos utilizando .items() (claves y valores)
    if opcion == 'a':
        print("\n--- *MENÚ DE LA CAFETERÍA *---")
        # Recorrido del diccionario accediendo tanto a la clave (producto) como al valor (precio)
        for indice, (producto, precio) in enumerate(cafeteria_menu.items(), start=1):
            print(f"{indice}. {producto.capitalize()} - ₡{precio:.3f}")
        print("-" * 30 + "\n")
        
    #.items(): Este método extrae tanto las claves (productos) como los valores (precios) del diccionario al mismo tiempo.
    #enumerate(..., start=1): Nos ayuda a generar un número autoincrementable (1, 2, 3...) para listar los productos en pantalla de forma ordenada.
    #.capitalize(): Convierte la primera letra del nombre del producto en mayúscula para que se vea más estético.
    #₡{precio:.3f}: Fuerza a que el número decimal se imprima siempre con exactamente dos decimales (por ejemplo, mostrará 2.50 en lugar de 2.5), cumpliendo con el formato monetario.