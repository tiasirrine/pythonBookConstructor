# Tia Orr
# Chpt 12

# define class called book


class Book:
    def __init__(self, title, author, publisher, publication_date):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.publication_date = publication_date

    def print_info(self):
        print('Book Information: ')
        print('   Book Title:', self.title)
        print('   Author:', self.author)
        print('   Publisher:', self.publisher)
        print('   Publication Date:', self.publication_date)

# define class called Encyclopedia derived from Book


class Encyclopedia(Book):
    def __init__(self, title, author, publisher, publication_date, edition, num_volumes):
        Book.__init__(self, title, author, publisher, publication_date)
        self.edition = edition
        self.num_volumes = num_volumes

    def print_info(self):
        print('Book Information: ')
        print('   Book Title:', self.title)
        print('   Author:', self.author)
        print('   Publisher:', self.publisher)
        print('   Publication Date:', self.publication_date)
        print('   Edition:', self.edition)
        print('   Number of Volumes: ', self.num_volumes)


# print lines statements that will obtain user input and be used when instantiated
if __name__ == '__main__':
    print('Enter Book Information')
    title = input('Enter title:')
    author = input('Enter author:')
    publisher = input('Enter publisher:')
    publication_date = input('Enter publication date:')
    print('\nEnter Encyclopedia Information')
    e_title = input('Enter title:')
    e_author = input('Enter author: ')
    e_publisher = input('Enter publisher:')
    e_publication_date = input('Enter publication date:')
    edition = input('Enter edition:')
    num_volumes = int(input('Enter number of volumes: '))

    # instantiate Book class
    my_book = Book(title, author, publisher, publication_date)
    my_book.print_info()
    # instantiate Encyclopedia class
    my_encyclopedia = Encyclopedia(
        title, author, publisher, publication_date, edition, num_volumes)
    my_encyclopedia.print_info()
