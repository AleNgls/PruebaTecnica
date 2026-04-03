import csv


def read_csv(csv_name):   

    books = set()

    try:
        with open(csv_name, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            
            for row in reader:

                title = row[0].strip()
                author = row[1].strip()
                year = row[2].strip()
                
                if not author:
                    author = "Author Unknown"
                
                if not year:
                    year = 0
                else:
                    try:
                        year= int(year)
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

    print("\nTITLE - AUTHOR - PUBLICATION YEAR\n")
    for title, author, year in books:
        print(f"{title} - {author} - {year}")


def search_by_author(books, author):
    results = []

    for book in books:
        if book[1].lower() == author.lower().strip():
            results.append(book)

    return results

def search_by_year(books, year):
    results = []

    for book in books:
        if book[2] == int(year.strip()):
            results.append(book)

    return results

def group_books(books):
    grouped = {}

    for title, author, year in books:

        if author == "Author Unknown":
            key = f"Author Unknown - Publication year {year}"
        else:
            key = author

        if key not in grouped:
            grouped[key] = []

        grouped[key].append((title, year))

    for key in sorted(grouped):
        print(f"\n{key}:")

        for title, year in sorted(grouped[key]):
            print(f"  - {title} - {year}")