import os

def main():
    os.system("cls" if os.name == "nt" else "clear")
    mensaje = "Bienvenido a comercial doña juanita"
    impuesto = 0.15
    limite = 2
    
    nombre = leer_cliente(mensaje)
    
    print("="*40)
    print("Datos de los productos")
    print("="*40)
    print(f"Se permiten {limite} productos distintos")
    
    porcentaje = float(input("digite el porcentaje de descuento: ")) / 100
    
    subtotal, descuento_compra, descuento_volumen, descuento_total, iva, total, cantidad1, precio1, cantidad2, precio2 = calcular_total(
        limite, porcentaje, impuesto
    )
    
    mostrar_factura(
        nombre, cantidad1, precio1, cantidad2, precio2, porcentaje, impuesto,
        subtotal, descuento_compra, descuento_volumen, descuento_total, iva, total
    )

def calcular_total(limite, porcentaje, impuesto):
    subtotal_acumulado, numero_unidades, cantidad1, precio1, cantidad2, precio2 = calcular_total_productos(limite)
    
    descuento_compra, descuento_volumen, descuento_total = calcular_descuento_total(
        subtotal_acumulado, porcentaje, numero_unidades
    )
    
    iva = calcular_iva(subtotal_acumulado, impuesto, descuento_total)
    
    total = subtotal_acumulado - descuento_total + iva
    
    return subtotal_acumulado, descuento_compra, descuento_volumen, descuento_total, iva, total, cantidad1, precio1, cantidad2, precio2

def calcular_total_productos(limite):
    cantidad1 = cantidad2 = 0
    precio1 = precio2 = 0.0
    
    numero_producto = 1
    while numero_producto <= limite:
        print(f"Producto {numero_producto}")
        if numero_producto == 1:
            cantidad1 = int(input("digite la cantidad de productos: "))
            precio1 = float(input("digite el precio del producto: "))
        elif numero_producto == 2:
            cantidad2 = int(input("digite la cantidad de productos: "))
            precio2 = float(input("digite el precio del producto: "))
            
        numero_producto += 1

    subtotal1 = calcular_subtotal(cantidad1, precio1)
    subtotal2 = calcular_subtotal(cantidad2, precio2)
    
    subtotal_acumulado = subtotal1 + subtotal2
    numero_unidades = cantidad1 + cantidad2
    
    return subtotal_acumulado, numero_unidades, cantidad1, precio1, cantidad2, precio2

def calcular_subtotal(cantidad, precio):
    return cantidad * precio

def calcular_descuento_total(subtotal, porcentaje, numero_unidades):
    descuento_compra = calcular_descuento_compra(subtotal, porcentaje)
    descuento_volumen = calcular_descuento_por_volumen(subtotal, numero_unidades)
    
    descuento_total = descuento_compra + descuento_volumen
    
    return descuento_compra, descuento_volumen, descuento_total

def calcular_descuento_compra(subtotal, porcentaje):
    return subtotal * porcentaje

def calcular_descuento_por_volumen(subtotal, numero_unidades):
    if numero_unidades >= 5:
        return subtotal * 0.05
    return 0.0

def calcular_iva(subtotal, impuesto, descuento):
    return (subtotal - descuento) * impuesto

def leer_cliente(mensaje):
    print(mensaje)
    print("="*40)
    nombre = input("digite el nombre del cliente: ")
    return nombre

def mostrar_factura(
    nombre, cantidad1, precio1, cantidad2, precio2, porcentaje, impuesto,
    subtotal, descuento_compra, descuento_volumen, descuento_total, iva, total
):
    print("\n" + "=" * 55)
    print("              FACTURA DE COMPRA")
    print("=" * 55)
    print(f"Cliente: {nombre}")
    print("-" * 55)
    print(f"Prod 1 | Cantidad: {cantidad1} | Precio: ${precio1:.2f}")
    print(f"Prod 2 | Cantidad: {cantidad2} | Precio: ${precio2:.2f}")
    print("-" * 55)
    print(f"Subtotal:                        ${subtotal:>10.2f}")
    print(f"Descuento de compra:            -${descuento_compra:>9.2f}")
    print(f"Descuento por volumen:          -${descuento_volumen:>9.2f}")
    print(f"Descuento total:                -${descuento_total:>9.2f}")
    print(f"IVA:                             ${iva:>10.2f}")
    print("=" * 55)
    print(f"TOTAL A PAGAR:                   ${total:>10.2f}")
    print("=" * 55)

if __name__ == "__main__":
    main()