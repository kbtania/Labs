# ЛАБОРАТОРНА РОБОТА № 9

## Завдання 1

#### Особиста бібліотека. Картотека домашньої бібліотеки: дані книги (автори, назва, видавництво і т.д.), розділ бібліотеки (спеціальна література, хобі, домашнє господарство і т.д.), походження книги і наявність на даний час. Організувати вибір книги за довільним запитом та проведення інвентаризації. Дані зберігаються в масиві. ###

```py
class Book:
    def __init__(self, author, title, publishing, availability='-'):
        self.author = author
        self.title = title
        self.publishing = publishing
        self.availability = availability

    def get_author(self):
        return self.author

    def get_title(self):
        return self.title

    def get_publishing(self):
        return self.publishing

    def get_availability(self):
        return self.availability

    def get_info(self):
        return "Name of book - {0}\n Author - {1}\n" \
               " Publishing house - {2}\n Availability - {3}".format(self.title, self.author,
                self.publishing, self.availability)


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, new_book):
        self.books.append(new_book)

    def get_book(self):
        return self.books


user_lib = []

spec_lit = Library()
spec_lit.add_book(Book('Swaroop', 'A Byte of Python', 'Create Space', 'available'))
spec_lit.add_book(Book('Paul Krugman', 'Microeconomics', 'Worth Publishers', 'not available'))
spec_lit.add_book(Book('Alvin Burns', 'Marketing Research', 'Worth Publishers', 'available'))
user_lib.append(spec_lit)

detective_liter = Library()
detective_liter.add_book(Book('Arthur Conan Doyle', 'The Hound of the Baskervilles', 'George Newnes', 'available'))
detective_liter.add_book(Book('Agatha Christie', 'Murder on the Orient Express', 'Collins Crime Club', 'available'))
detective_liter.add_book(Book('Dorothy L', 'Whose Body?', 'Fisher Unwin', 'not available'))
user_lib.append(detective_liter)

kids_liter = Library()
kids_liter.add_book(Book('Lewis Carroll', 'Alice in Wonderland', 'Appleton Company. ', 'available'))
kids_liter.add_book(Book('J K Rowling', 'Harry Potter', 'Bloomsbury', 'not available'))
kids_liter.add_book(Book('Mark Twain', 'The Adventures of Tom Sawyer', 'American Publishing', 'available'))
kids_liter.add_book(Book('Rudyard Kipling', 'The Jungle Book', 'Macmillan', 'available'))
user_lib.append(kids_liter)
book = Library()


while True:
    print('Search by:\n --author\n --title\n --publishing\n '
          '--check books\n --add book\n --all books\n --exit')
    choice = input('My choice: ')
    if choice == 'exit':
        break

    elif choice == 'add':
        book.add_book(Book(input('Author: '), input('Title: '), input('Publishing: '), input('Availability: ')))
        user_lib.append(book)
        continue

    elif choice == 'publishing':
        user_publishing = input('Publishing: ')
        for section in user_lib:
            for book in section.get_book():
                if book.get_publishing() == user_publishing:
                    print('\n', book.get_info())

    elif choice == 'author':
        user_author = input('Author: ')
        for section in user_lib:
            for book in section.get_book():
                if book.get_author() == user_author:
                    print('\n', book.get_info())

    elif choice == 'title':
        user_title = input('Title: ')
        for section in user_lib:
            for book in section.get_book():
                if book.get_title() == user_title:
                    print('\n', book.get_info())

    elif choice == 'check books':
        avail = input('Available: ')
        for section in user_lib:
            for book in section.get_book():
                if book.get_availability() == avail:
                    print('\n', book.get_info())

    elif choice == 'all books':
        for section in user_lib:
            for book in section.get_book():
                print('\n', book.get_info())
    else:
        print('Try again!')
```
