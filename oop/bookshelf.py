
class Bookshelf(object):
    infos = ['author', 'title', 'isbn']

    def __init__(self):
        self.books = []
        self.borrowed = set()
        self.index = {}

        for s in infos:
            self.index[s] = {}

    def add_book(self, book):
        self.books.append(book)
        for s in infos:
            entry = self.index[s].get(book.author, [])
            if not entry:
                self.index[s][book.author] = [book]
            else:
                entry.append(book)

    def lookup_by(self, info, query):
        return self.index[info][query]

    def checkout(self, name, book):
        if book not in self.borrowed:
            self.borrowed.add(book)
            self.books.remove(book)
            return True
        else:
            return False


class book(object):

    def __init__(self, title, author, isbn):
        self.title = title
        self.isbn = isbn
        self.author = author
