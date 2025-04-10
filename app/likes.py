from app.utils import cargar_json, guardar_json

def dar_like(from_user, to_user):
    likes = cargar_json('likes.json')
    for like in likes:
        if like['from'] == to_user and like['to'] == from_user:
            return "¡Match encontrado!"
    likes.append({'from': from_user, 'to': to_user})
    guardar_json('likes.json', likes)
    return "Like registrado exitosamente"

def verificar_match(from_user, to_user):
    likes = cargar_json('likes.json')
    for like in likes:
        if like['from'] == to_user and like['to'] == from_user:
            return True
    return False
