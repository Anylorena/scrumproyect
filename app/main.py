from app.auth import registrar_usuario, iniciar_sesion
from app.imagenes import subir_imagen, ver_imagenes
from app.likes import dar_like

def menu():
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Subir imagen")
    print("4. Ver imágenes")
    print("5. Dar like")
    print("6. Salir")

def main():
    while True:
        menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            username = input("Ingrese su nombre de usuario: ")
            password = input("Ingrese su contraseña: ")
            print(registrar_usuario(username, password))
        elif opcion == "2":
            username = input("Ingrese su nombre de usuario: ")
            password = input("Ingrese su contraseña: ")
            if iniciar_sesion(username, password):
                print("Inicio de sesión exitoso")
            else:
                print("Usuario o contraseña incorrectos")
        elif opcion == "3":
            username = input("Ingrese su nombre de usuario: ")
            archivo_imagen = input("Ingrese la ruta de la imagen: ")
            print(subir_imagen(username, archivo_imagen))
        elif opcion == "4":
            imagenes = ver_imagenes()
            print("Imágenes disponibles:")
            for imagen in imagenes:
                print(imagen)
        elif opcion == "5":
            from_user = input("Tu nombre de usuario: ")
            to_user = input("Usuario al que quieres dar like: ")
            print(dar_like(from_user, to_user))
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
