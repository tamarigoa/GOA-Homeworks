secret_pass="goa1234"
user_pass=""

tries=3

while tries >= 0 or user_pass !=secret_pass:
    user_pass=input("enter your password(you have "+ str(tries)+ "tries left)")
    tries=tries-1
    if user_pass==secret_pass:
        print("Good job!")
    elif tries == 0:
        print("no more tries left")
    else:
        print("try gaain")