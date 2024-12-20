# def sum_cubes(n):
#     total = 0
#     for i in range(1, n + 1):
#         total += i ** 3
#     return total






# def most_frequent_item_count(collection):
#     if not collection:
#         return 0
#     count = (collection) 
#     return max(count.values()) 


# def disarium_number(number):
#     digits = str(number)
#     total = 0
#     for i, digit in enumerate(digits):
#         total += int(digit) ** (i + 1)  
#     if total == number:
#         return "Disarium !!"
#     else:
#         return "Not !!"



# def in_asc_order(arr):
#     if len(arr) <= 1:
#         return True
#     for i in range(len(arr) - 1):
#         if arr[i] > arr[i + 1]:
#             return False
    
#     return True 



# def max_multiple(divisor, bound):
#     return (bound // divisor) * divisor



# def sum_dig_pow(a, b):
#     result=[]
#     for num in range(a, b + 1):
#         digits = [int(digit) for digit in str(num)]
#         sum_of_powers = sum(digit ** (index + 1) for index, digit in enumerate(digits))
#         if sum_of_powers == num:
#             result.append(num)
#     return result