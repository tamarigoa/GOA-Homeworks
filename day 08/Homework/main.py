num=0
while num < 50:
    num=num+1
    print(num)
    

    my_password=("1234")
password=input("Guess my password")
while password !=my_password:
    print("wrong")
    password=input("Guess my password")
print("You are correct")