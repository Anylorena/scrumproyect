import json
from app.utils import cargar_json, guardar_json

def registrar_usuario(username, password):
    usuarios = cargar_json('users.json')
    for usuario in usuarios:
        if usuario['username'] == username:
            return "El usuario ya existe"
    usuarios.append({'username': username, 'password': password})
    guardar_json('users.json', usuarios)
    return "Usuario registrado exitosamente"

def iniciar_sesion(username, password):
    usuarios = cargar_json('users.json')
    for usuario in usuarios:
        if usuario['username'] == username and usuario['password'] == password:
            return True
    return False
