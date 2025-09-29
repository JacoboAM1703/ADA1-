import csv
# Funcion d merge pra combinar listas ordenadaas
def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        # como ordenarlos:
        # 1 Calificación de mayorr a menor
        # 2 Si hay empate precio de menor a mayor
        if (left[i]["calificacion"] > right[j]["calificacion"]) or \
           (left[i]["calificacion"] == right[j]["calificacion"] and left[i]["precio"] < right[j]["precio"]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Agregar lo que lesobra
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Función merge_sort (Divide y Vencerss)



def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    mid = len(lista) // 2
    left = merge_sort(lista[:mid])
    right = merge_sort(lista[mid:])
    return merge(left, right)

# aqui es donde se lee el archivo CSV
productos = []
with open("productos (2).csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        productos.append({
            "id": int(row["id"]),
            "nombre": row["nombre"],
            "precio": float(row["precio"]),
            "calificacion": int(row["calificacion"]),
            "stock": int(row["stock"])
        })

print(f"Total de productos leídos: {len(productos)}")

# Ordenar con Merge Sort
productos_ordenados = merge_sort(productos)

# Mostrar los 10 mejores productos pero si quiere puede hacer que le muestree ordenadosm los 5k
print("\n=== los 10 mejores productos ===")
for p in productos_ordenados[:10]:
    print(f"ID: {p['id']}, Nombre: {p['nombre']}, "
          f"Calificación: {p['calificacion']}, Precio: {p['precio']}, Stock: {p['stock']}")
