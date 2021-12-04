import time
start_time = time.time()

desired_book = input()
books_count = 0
found_it = False
book = input()

while book != 'No More Books':

    if book == desired_book:
        found_it = True
        break

    book = input()
    books_count += 1

if found_it:
    print(f"You checked {books_count} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {books_count} books.")
