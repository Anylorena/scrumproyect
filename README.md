# igtimatch

Una mini app de estilo Pinterest creada con Python donde los usuarios pueden:

- Registrarse e iniciar sesión.
- Ver imágenes de todo tipo subidas por otros usuarios.
- Darle like a las imágenes.
- Subir sus propias imágenes.
- Hacer “match” con otros usuarios si hay likes mutuos.

---

## 🚀 Objetivo del Proyecto

Crear una versión simple y local de una red social de imágenes sencillas usando sólo Python, sin bases de datos complicadas, ideal para programadores en formación.

---

## 🧩 Funcionalidades

### 👤 Registro e Inicio de Sesión
- Los usuarios se registran con un nombre de usuario y contraseña.
- Los datos se guardan en un archivo `users.json`.

### 📹 Subir imagen
- El usuario puede seleccionar un archivo de imagen local (.jpg).
- La imagen se copia a la carpeta `/imágenes` y se asocia al usuario en el archivo JSON.

### 🎬 Ver imágenes
- El usuario puede ver imágenes de otros usuarios en pantalla.
- Cada imagen tiene botones para interactuar:
  - 👍 **Like**: Al darle like a una imagen, se guarda el registro en `likes.json` con los detalles:
    - **from**: El usuario que da el like.
    - **to**: El dueño de la imagen.
  - ⏭️ **Siguiente**: Para pasar a la siguiente imagen.
  - ❤️ **Dar Like**: Función para dar like a la imagen mostrada.

### 🔁 Match
- Cuando dos usuarios se han dado like mutuamente, se considera un "match".
- El match se guarda en el archivo `matches.json` con el siguiente formato:
  ```json
  {
    "user1": "ana",
    "user2": "juan"
  }
