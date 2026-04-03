import csv


def read_csv(csv_name):   

    books = set()

    try:
        with open(csv_name, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            
            for row in reader:

                title = row[0]
                author = row[1]
                year = row[2]
                
                if not author.strip():
                    author = "Author Unknown"
                
                if not year.strip():
                    year = 0
                else:
                    try:
                        year = int(year)
                        if year < 0:
                            year = 0
                    except:
                        year = 0

                books.add((title, author, year))

    except FileNotFoundError:
        print(f"Error: file named '{csv_name}' does not exist.")
        return None

    return books

def list_csv(books):
    if not books:
        print("No books to display.")
        return

    for title, author, year in books:
        print(f"{title}, {author}, {year}")


def search_by_author(books, author):
    results = []

    for book in books:
         if book[1].lower().strip() == author.lower().strip():
            results.append(book)

    return results

def search_by_year(books, year):
    results = []

    for book in books:
         if book[2].strip() == year.strip():
            results.append(book)

    return results