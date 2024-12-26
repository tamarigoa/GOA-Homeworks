# def dont_give_me_five(start,end):
#     result = 0
#     for i in range(start, end + 1):
#         if "5" not in str(i):
#             result += 1
#     return result

# def capitalize(s):
#     even = ''.join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s))
    
#     odd = ''.join(c.upper() if i % 2 == 1 else c.lower() for i, c in enumerate(s))
    
#     return [even, odd]

# def fizzbuzz(n):
#     result = []
#     for i in range(1, n + 1):
#         if i % 3 == 0 and i % 5 == 0:
#             result.append("FizzBuzz")
#         elif i % 3 == 0:
#             result.append("Fizz")
#         elif i % 5 == 0:
#             result.append("Buzz")
#         else:
#             result.append(i)
#     return result



# def up_array(arr):
#     def up_array(arr):
#         if not arr:
#             return None
        

#     if any(num < 0 or num > 9 for num in arr):
#         return None
#     num = 0
#     for digit in arr:
#         num = num * 10 + digit
    
#     num += 1

#     result = []
#     while num > 0:
#         result.insert(0, num % 10)
#         num //= 10

#     while len(result) < len(arr):
#         result.insert(0, 0)
        
#     if len(result) < len(arr) + 1:
#         return result
#     elif result[0] == 1 and all(x == 0 for x in result[1:]):
#         return result
#     else:
#         return None