# def compute_sum(n):
#     sum = 0
    
#     for number in range(1, n + 1):
#         str_number = str(number)
#         if len(str_number) > 1:
#             for char in str_number:
#                 sum += int(char)
#         else:
#             sum += number


# def str_sum(arr):
#     result = ""
#     minus = False
    
#     for number in arr:
#         if "-" in str(number):
#             result += str(number).replace("-", "")
#             minus = True
#         else:
#             result += str(number)
    
#     if minus:
#         return -int(result)
#     else:
#         return int(result)

# def sum_arrays(array1,array2):
#     if not array1 and not array2:
#         return []
#     if not array1:
#         return array2
#     if not array2:
#         return array1
    
#     result = []
    
#     sum = str_sum(array1) + str_sum(array2)
    
#     if sum >= 0:
#         for char in str(sum):
#             result.append(int(char))
#     else:
#         for char in str(sum)[1:]:
#             result.append(int(char))
#         result[0] *= -1
    
    
#     return result