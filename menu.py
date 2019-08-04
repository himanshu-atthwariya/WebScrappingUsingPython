from app import lists_books

MENU="""Enter:
- 'a' to look at best 5 books
- 'b' to look at most inexpensive 5 books
- 'c' to look at next book in catalogue
- 'd' to print all books
- 'q' to quit
Enter your choice:
"""

# CHOICES={
#     'a':"print_best_books",
#     'b':"print_inexpensive_books",
#     'c':"print_next_book()",
#     'd':"print_all_books"
# }

def menu():
    while True:
        user_input=input(MENU)
        if user_input =='a':
            print_best_books()
        elif user_input=='b':
            print_inexpensive_books()
        elif user_input=='c':
            print_next_book()
        elif user_input=='d':
            print_all_books()
        elif user_input=='q':
            print("STOPPING PROGRAM.....")
            break
        else:
            print("Invalid Input. Please Try Again.")
        print()

def print_best_books():
    best_books= sorted(lists_books, key=lambda x: x.rating * -1)[:5]
    for book in best_books:
        print(book)

def print_inexpensive_books():
    inexpesive_books= sorted(lists_books, key=lambda x:x.price)[:5]
    for book in inexpesive_books:
        print(book)

gen_book=(book for book in lists_books)
def print_next_book():
    print(next(gen_book))

def print_all_books():
    for book in lists_books:
        print(book)

menu()