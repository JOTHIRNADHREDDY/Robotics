number = int(input("enter a number :"))
if number % 3 == 0 :
    print("FIzz")
elif number % 5 == 0 :
    print("Buzz")
elif number % 3 == 0 and number % 5 == 0 :
    print("FIzzBuzz")
else :
    print(number)
    