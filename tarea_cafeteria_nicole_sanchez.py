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
    "jugo de naranja": 0.850,
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