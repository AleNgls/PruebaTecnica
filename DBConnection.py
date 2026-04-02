def save_books_to_db(books):
    import sqlite3

    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT,
        year INTEGER
    )
    """)

    for book in books:
        cursor.execute(
            "INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
            book
        )

    connection.commit()
    connection.close()