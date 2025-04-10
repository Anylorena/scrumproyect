import os
import shutil

def subir_imagen(username, archivo_imagen):
    if not os.path.exists('imagenes'):
        os.makedirs('imagenes')
    
    ruta_destino = os.path.join('imagenes', f"{username}_{os.path.basename(archivo_imagen)}")
    shutil.copy(archivo_imagen, ruta_destino)
    return f"Imagen subida exitosamente: {ruta_destino}"

def ver_imagenes():
    imagenes = [f for f in os.listdir('imagenes') if f.endswith('.jpg')]
    return imagenes
