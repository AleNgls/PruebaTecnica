from CSVReader import read_csv
from DBConnection import save_books_to_db

def menu():
    print("\n=== MENU ===")
    print("1. Leer un archivo CSV")
    print("2. Guardar archivo CSV leido")
    print("3. Salir")


def main():
    books = None
    csv_name = ""

    while True:
        menu()
        option = input("Elija una opción: ")

        if option == "1":
            while True:
                csv_name = input("Ingrese el nombre del archivo: ")
                books = read_csv(csv_name)

                if books is None:
                    print("Archivo inválido. Intente nuevamente.")
                else:
                    print("Libros ingresados.")
                    break

        elif option == "2":
            if books is None:
                print("Debe ingresar el nombre del archivo CSV primero.")
            else:
                save_books_to_db(books)
                print("Libros guardados en la base de datos correctamente.")

        elif option == "3":
            print("Saliendo...")
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()