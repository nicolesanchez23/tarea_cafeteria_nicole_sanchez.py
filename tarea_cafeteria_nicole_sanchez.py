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
    "pastel de frutos rojos": 1.500,
    "jugo de naranja": 1.000,
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
        
    # .items(): Este método extrae tanto las claves (productos) como los valores (precios) del diccionario al mismo tiempo.
    # enumerate(..., start=1): Nos ayuda a generar un número autoincrementable (1, 2, 3...) para listar los productos en pantalla de forma ordenada.
    # .capitalize(): Convierte la primera letra del nombre del producto en mayúscula para que se vea más estético.
    # ₡{precio:.3f}: Fuerza a que el número decimal se imprima siempre con exactamente dos decimales (por ejemplo, mostrará 2.50 en lugar de 2.5), cumpliendo con el formato monetario.
  
   # Opción B: Agregar un producto al pedido
    elif opcion == 'b':
        print("\n--- AGREGAR PRODUCTO A TU PEDIDO ---")
        producto_ingresado = input("Ingresa el nombre del producto que deseas agregar: ").lower().strip()
        
        # Búsqueda del producto utilizando un bucle for con una estructura for/else
        producto_encontrado = False
        for producto_menu in cafeteria_menu:
            if producto_menu == producto_ingresado:
                producto_encontrado = True
                break # Rompe el bucle al encontrar el producto
        else:
            # Este bloque se ejecuta únicamente si el bucle termina sin hacer un break
            print(f"Lo sentimos, '{producto_ingresado}' no existe en nuestro menú.\n")
            continue
        
        # 5. Solicitar la cantidad asegurando que sea un número entero mayor a cero
        while True:
            try:
                cantidad = int(input(f"Ingresa la cantidad para '{producto_ingresado}': "))
                if cantidad > 0:
                    break
                print("La cantidad debe ser mayor a cero.")
            except ValueError:
                print("Por favor, ingresa un número entero válido.")
        
        # Agregar o actualizar el producto en el diccionario del pedido
        if producto_ingresado in pedido_actual:
            pedido_actual[producto_ingresado] += cantidad
        else:
            pedido_actual[producto_ingresado] = cantidad
            
        print(f"¡Se han agregado {cantidad} unidad(es) de '{producto_ingresado}' a tu pedido!\n") 
       
        #Opcion C: Ver el pedido actual
        
    elif opcion == 'c':
        print("\n--- TU PEDIDO ACTUAL ---")
        # 6. Validar si el pedido está vacío
        if not pedido_actual:
            print("Tu pedido actualmente está vacío.\n")
        else:
            subtotal_parcial = 0.0
            for producto, cantidad in pedido_actual.items():
                precio_unitario = cafeteria_menu[producto]
                subtotal_producto = precio_unitario * cantidad
                subtotal_parcial += subtotal_producto
                print(f"- {producto.capitalize()} | Cantidad: {cantidad} | Subtotal: ${subtotal_producto:.2f}")
            print(f"Subtotal acumulado: ₡{subtotal_parcial:.2f}\n")
            
    # if not pedido_actual:: Comprueba si el diccionario del pedido está vacío. Si lo está, avisa al usuario.
    #Cálculo de subtotales: Recorre cada producto seleccionado, busca su precio en el menú original, lo multiplica por la cantidad pedida e imprime el detalle acumulando un subtotal general parcial
    
    # Opción D: Finalizar el pedido y salir
    elif opcion == 'd':
        if not pedido_actual:
            print("\nNo tienes ningún producto en tu pedido. ¡Esperamos verte pronto!")
            break
        
        print("\n--- FINALIZAR PEDIDO ---")
        
        # Calcular el subtotal general antes de la propina
        subtotal_general = 0.0
        for producto, cantidad in pedido_actual.items():
            subtotal_general += cafeteria_menu[producto] * cantidad
            
        #Solicitar el porcentaje de propina validando el rango de 0 a 100
        while True:
            try:
                porcentaje_propina = float(input("Ingresa el porcentaje de propina que deseas dejar (0 a 100): "))
                if 0 <= porcentaje_propina <= 100:
                    break
                print("El porcentaje debe estar entre 0 y 100.")
            except ValueError:
                print("Por favor, ingresa un número válido.")
                
        # Cálculos monetarios finales
        monto_propina = subtotal_general * (porcentaje_propina / 100)
        total_a_pagar = subtotal_general + monto_propina
        
        # Mostrar el resumen detallado utilizando f-strings y formato de dos decimales
        print("\n" + "="*40)
        print("          RESUMEN DE TU COMPRA          ")
        print("="*40)
        print(f"Cliente: {nom_cliente.capitalize()}")
        print("Detalle:")
        for producto, cantidad in pedido_actual.items():
            costo_item = cafeteria_menu[producto] * cantidad
            print(f"  • {producto.capitalize()} (x{cantidad}) - ${costo_item:.2f}")
        print("-" * 40)
        print(f"Subtotal:       ${subtotal_general:.2f}")
        print(f"Propina ({porcentaje_propina}%): ${monto_propina:.2f}")
        print(f"Total a pagar:  ${total_a_pagar:.2f}")
        print("="*40)
        print("¡Gracias por tu compra en la Cafetería! ¡Que tengas un excelente día!\n")
        
        # Terminar el bucle principal y cerrar el programa
        break