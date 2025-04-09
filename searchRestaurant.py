import json
import os

ARCHIVO_JSON = 'restaurantes.json'
CATEGORIAS = ['italiano', 'comida_rapida', 'comida_tipica']

def cargar_datos():
    if not os.path.exists(ARCHIVO_JSON):
        print("❌ El archivo de restaurantes no existe. Primero registra algunos restaurantes.")
        return None
    with open(ARCHIVO_JSON, 'r') as f:
        return json.load(f)

def mostrar_restaurantes_por_categoria():
    data = cargar_datos()
    if data is None:
        return

    print(f"📂 Categorías disponibles: {', '.join(CATEGORIAS)}")
    categoria = input("📋 Ingresa la categoría que deseas consultar: ").strip().lower()

    if categoria not in CATEGORIAS:
        print("❌ Categoría inválida.")
        return

    print(f"\n--- 🍽️ Restaurantes en la categoría '{categoria}' ---")

    for rango, restaurantes in data[categoria].items():
        titulo = "💸 Menos de 50k" if rango == "menos_50k" else "💎 Más de 50k"
        print(f"\n{titulo}:")
        if not restaurantes:
            print("  (No hay restaurantes en este rango.)")
        else:
            for r in restaurantes:
                print(f"  - {r['nombre']} | Dirección: {r['direccion']} | Precio: ${r['precio']:,}")

def mostrar_restaurantes_por_rango():
    data = cargar_datos()
    if data is None:
        return

    print("\n🤑 Rango de precios disponibles:")
    print("1. Menos de 50k")
    print("2. Más de 50k")
    opcion = input("👉 Elige una opción: ").strip()

    if opcion == "1":
        rango = "menos_50k"
        titulo_rango = "💸 Menos de 50k"
    elif opcion == "2":
        rango = "mas_50k"
        titulo_rango = "💎 Más de 50k"
    else:
        print("❌ Opción inválida.")
        return

    print(f"\n--- {titulo_rango} en todas las categorías ---")

    encontrados = False
    for categoria, rangos in data.items():
        restaurantes = rangos[rango]
        if restaurantes:
            print(f"\n📂 Categoría: {categoria}")
            for r in restaurantes:
                print(f"  - {r['nombre']} | Dirección: {r['direccion']} | Precio: ${r['precio']:,}")
            encontrados = True

    if not encontrados:
        print("⚠️ No se encontraron restaurantes en ese rango de precio.")

def menu_consulta():
    while True:
        print("\n--- 🔍 CONSULTAR RESTAURANTES ---")
        print("1. Consultar por categoría")
        print("2. Buscar por rango de precio")  # Esta es ahora la opción 2
        print("3. Salir")

        opcion = input("👉 Elige una opción: ").strip()
        if opcion == "1":
            mostrar_restaurantes_por_categoria()
        elif opcion == "2":
            mostrar_restaurantes_por_rango()
        elif opcion == "3":
            print("👋 ¡Consulta finalizada!")
            break
        else:
            print("❌ Opción inválida.")

if __name__ == '__main__':
    menu_consulta()
2