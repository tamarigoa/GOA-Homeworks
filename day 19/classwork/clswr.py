numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = 0
odds = 0
index = 0
while index < len(numbers):
    if numbers[index] % 2 == 0: 
        evens += numbers[index]
    else:  
        odds += numbers[index]
    index += 1

if evens > odds:
    print(evens)
else:
    print(odds)