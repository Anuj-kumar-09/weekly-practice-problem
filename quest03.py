# Problem 3: Library Borrow Checker
# • Maintain a dictionary of available books (title → quantity).
# • Take user input for borrowing a book.
# • If the book exists and quantity > 0, issue it (reduce quantity by 1).
# • If not available, show “Out of stock” or “Not found”.
# • After all operations, write back the updated inventory to a file library.txt.

dict={
    "physics":5,
    "chemistry":6,
    "math":5
 }

b=input("enter your book name :-- ").lower()
if b in dict:
    if dict[b]>=1:
        print("book is available")
        l=input("are you want issue the book yes/no :--").lower()
        if l=="yes":
            dict[b]-=1
            print("you issued the book ",b)
        else:
            print("you cancel the book issue")
    else:
        print("out of stock")
else:
    print("this book is not in library")
b=str(dict)
print(b)
print(type(b))
with open("library.txt","w") as f:
    m=f.write(b)
