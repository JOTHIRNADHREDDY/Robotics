#Phone Book


phone_book = {}
while True:
    name = input("Enter a name (or done to finish):")
    if name.lower() == "done":
        break   
    number = input("Enter the phone number: ")
    phone_book[name] = number
print("Your phone book:", phone_book)

