list = []

def addList(list):
    while True:
    
        list.append({
            "Descripción": input("Descripción: "),
            "Fecha Límite": input("Fecha Límite: "),
            "Prioridad": input("Prioridad: ")
            }
        )
        continuar = input("¿Quieres agregar otra tarea? (s para sí, cualquier otra tecla para salir): ")
        if continuar.lower() != 's':
            break

print(addList(list))
