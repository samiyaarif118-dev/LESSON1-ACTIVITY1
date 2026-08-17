books = ["powerless","atomic habit","harry potter","the hobbit"]
book_count = [1,7,9,0]
library = {
    book: count for book, count in zip (books, book_count)
}
print("library stock : ", library)

available_book = [book for book in books if library[book]>0]
print("book available:", available_book)

reader_choice = input("Enter your book")

if reader_choice not in library or library[reader_choice] == 0:
    print(reader_choice, "book is not available")
    exit()

late_fee = [2,7,4,3]
extra_fee = int(input("Enter fee"))

updated_fee = list(map(lambda fee: fee + extra_fee,late_fee ))
print("updated late fee: ", updated_fee)

book_index = books.index(reader_choice)
chosen_fee = updated_fee[book_index]
print("late fee for:",reader_choice, "after update:", chosen_fee)

library[reader_choice] = library[reader_choice] -1 
print(reader_choice, "borrowed remaining copies:",library[reader_choice])

print("borrowed book:", reader_choice)
print("late fee:", chosen_fee)
print("updated library stock:",library)

