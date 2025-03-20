personas = [
    {"Nombre": "Juan", "Edad":  24},
    {"Nombre": "Pedro", "Edad":  25},
    {"Nombre": "Ana", "Edad":  26},
    {"Nombre": "Luis", "Edad":  27}
]


print(personas[0])
print(personas[1]["Edad"])
print("---")
for persona in personas:
    for key, value in persona.items():
        print(f"{key}: {value}")  

