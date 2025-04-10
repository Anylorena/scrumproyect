import json

def cargar_json(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def guardar_json(nombre_archivo, data):
    with open(nombre_archivo, 'w') as f:
        json.dump(data, f)
