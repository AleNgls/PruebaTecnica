from CSVReader import read_csv, list_csv, search_by_author, search_by_year
from DBConnection import save_books_to_db

def menu():
    print("\n=== MENU ===")
    print("1. Read a CSV file")
    print("2. Save books to database")
    print("3. Show list of book entries")
    print("4. Search by author")
    print("5. Search by publication year")
    print("6. Exit")


def main():
    books = None
    csv_name = ""

    while True:
        menu()
        option = input("Choose an option: ")

        if option == "1":
            while True:
                csv_name = input("Enter file name: ")
                books = read_csv(csv_name)

                if books is None:
                    print("Invalid file name. Try again.")
                else:
                    print("Books processed succesfully.")
                    break

        elif option == "2":
            if books is None:
                print("-You must enter a CSV file name fist.-")
            else:
                save_books_to_db(books)
                print("Books succesfully saved to the database.")

        elif option == "3":
            if books is None:
                print("-You must enter a CSV file name fist.-")
            else:
                list_csv(books)

        elif option == "4":
            if books is None:
                print("-You must enter a CSV file name fist.-")
            else:
                author = input("Enter author name: ")
                books_by_author = search_by_author(books, author)
                list_csv(books_by_author)

        elif option == "5":
            if books is None:
                print("-You must enter a CSV file name fist.-")
            else:
                year = input("Enter publication year: ")
                books_by_year = search_by_year(books, year)
                list_csv(books_by_year)

        elif option == "6":
            print("Closing...")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()