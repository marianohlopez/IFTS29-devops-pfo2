import requests

BASE_URL = "http://server:5000"  # apunta al servicio dockerizado


def registrar_usuario():
    usuario = input("Ingrese nombre de usuario: ")
    contraseña = input("Ingrese contraseña: ")
    res = requests.post(f"{BASE_URL}/registro",
                        json={"usuario": usuario, "contraseña": contraseña})
    print("Respuesta:", res.json())


def login_usuario():
    usuario = input("Ingrese nombre de usuario: ")
    contraseña = input("Ingrese contraseña: ")
    res = requests.post(f"{BASE_URL}/login",
                        json={"usuario": usuario, "contraseña": contraseña})
    print("Respuesta:", res.json())


def ver_tareas():
    res = requests.get(f"{BASE_URL}/tareas")
    print("Respuesta HTML:\n")
    print(res.text)


def menu():
    while True:
        print("\n--- Cliente ---")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Ver tareas")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            login_usuario()
        elif opcion == "3":
            ver_tareas()
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    menu()
