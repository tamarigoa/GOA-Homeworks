secret_num=9
user_num=0
while user_num != secret_num:
    user_num=int(input("enter number"))

    if user_num > secret_num:
        print("your number is high")
    elif user_num<secret_num:
        print("your number is low")
    else:
        print("You guessed")