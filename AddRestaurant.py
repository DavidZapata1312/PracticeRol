import json
import os

ARCHIVO_JSON = 'restaurantes.json'

CATEGORIAS = ['italiano', 'comida_rapida', 'comida_tipica']
RANGOS = {
    'menos_50k': lambda precio: precio <= 50000,
    'mas_50k': lambda precio: precio > 50000
}

def inicializar_archivo():
    if not os.path.exists(ARCHIVO_JSON):
        data = {cat: {"menos_50k": [], "mas_50k": []} for cat in CATEGORIAS}
        with open(ARCHIVO_JSON, 'w') as f:
            json.dump(data, f, indent=4)

def cargar_datos():
    with open(ARCHIVO_JSON, 'r') as f:
        return json.load(f)

def guardar_datos(data):
    with open(ARCHIVO_JSON, 'w') as f:
        json.dump(data, f, indent=4)

def nombre_ya_existe(nombre, data):
    for categoria in data.values():
        for rango in categoria.values():
            for restaurante in rango:
                if restaurante["nombre"].lower() == nombre.lower():
                    return True
    return False

def registrar_restaurante():
    nombre = input("🍽️  Nombre del restaurante: ").strip()
    direccion = input("📍 Dirección del restaurante: ").strip()
    print(f"📂 Categorías disponibles: {', '.join(CATEGORIAS)}")
    categoria = input("📋 Ingresa la categoría: ").strip().lower()

    if categoria not in CATEGORIAS:
        print("❌ Categoría inválida. Intenta de nuevo.")
        return

    try:
        precio = int(input("💰 Precio promedio por plato (en pesos): "))
    except ValueError:
        print("❌ Precio inválido. Debe ser un número.")
        return

    data = cargar_datos()

    if nombre_ya_existe(nombre, data):
        print(f"⚠️ El restaurante '{nombre}' ya está registrado. No se permiten duplicados.")
        return

    for rango, criterio in RANGOS.items():
        if criterio(precio):
            data[categoria][rango].append({
                "nombre": nombre,
                "direccion": direccion,
                "precio": precio
            })
            print(f"✅ Restaurante '{nombre}' registrado exitosamente en '{categoria}' bajo el rango '{rango}'.")
            break

    guardar_datos(data)

def menu():
    inicializar_archivo()
    while True:
        print("\n--- 📖 MENÚ DE REGISTRO DE RESTAURANTES ---")
        print("1. Registrar restaurante")
        print("2. Salir")
        opcion = input("👉 Elige una opción: ").strip()
        if opcion == "1":
            registrar_restaurante()
        elif opcion == "2":
            print(" ¡Hasta luego!")
            break
        else:
            print(" Opción no válida.")

if __name__ == '__main__':
    menu()
