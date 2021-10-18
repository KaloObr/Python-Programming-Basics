favorite_book = input()
bookshelf_capacity = int(input())
number_of_books_checked = 0

book_found = False

while bookshelf_capacity:
    current_book = input()

    if current_book == favorite_book:
        book_found = True
        break

    number_of_books_checked += 1
    bookshelf_capacity -= 1

if book_found:
    print(f"You checked {number_of_books_checked} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {number_of_books_checked} books.")
