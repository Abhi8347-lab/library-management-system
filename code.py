class book:
    def __init__(self,tittle,author,copies):
        self.tittle=tittle
        self.author=author
        self.copies=copies
        self.copies__avilable=copies
class person:
    def __init__(self,name):
        self.name=name
class member(person):
    def borrow(self,book):
        if book.copies__avilable>0:
            book.copies__avilable -=1
            print(f'{self.name} borrowed {book.tittle}')
        else:
            print('book not available')
    def return_book(self,book):
        book.copies__avilable+=1
        print(f'{self.name} have returned {book.tittle}')
    def check_copies(self) :
        return book.copies__avilable

class librarian(person):
      def add_book(self, library, book):
             library.books.append(book)


class library:
          def __init__(self,):
             self.books=[]
             self.member=[]
          def self_member(self,member):
              self.member.append(member)

          def get_book_by_author(self, author):
              result = []
              for b in self.books:
                  if b.author == author:
                      result.append(b)
              return result
lib = library()

b1 = book("1984", "Orwell", 2)
asha = member("Asha")
rao = librarian("Mr. Rao")

rao.add_book(lib, b1)
asha.borrow(b1)
asha.borrow(b1)
asha.borrow(b1)
asha.return_book(b1)
print(b1.copies__avilable)
