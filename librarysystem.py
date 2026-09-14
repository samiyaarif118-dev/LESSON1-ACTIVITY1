class Book:

  def __init__(self, title, author):
    self.title = title
    self.author = author
    self.is_borrowed = False

  def borrow(self):

    if self.is_borrowed:
      print(f"Sorry, '{self.title}' is already borrowed!")
    else:
      self.is_borrowed = True
      print(f"You have successfully borrowed '{self.title}'.")

  def return_book(self):

    if not self.is_borrowed:
      print(f" '{self.title}' was not borrowed.")
    else:
      self.is_borrowed = False
      print(f"You have returned '{self.title}'.")

  def __str__(self):
    status = "Borrowed" if self.is_borrowed else "Available"
    return f"{self.title} by {self.author} [{status}]"

book1 = Book("The Girl with the Dragon Tattoo", "Stieg Larsson")
book2 = Book("Dune", "Frank Herbert")
book3 = Book("Brave New World", "Aldous Huxley")

print("Welcome to library system")

print(book1)
print(book2)
print(book3)

book1.borrow()
book1.borrow()  

book2.return_book()

book1.return_book()

print("Final Status of Books:")
print(book1)
print(book2)
print(book3)

