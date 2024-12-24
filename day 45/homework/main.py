# def valid_phone_number(phone_number):
#     if len(phone_number) != 13:
#         return False
    
#     if phone_number[0] != '(' or phone_number[4] != ')':
#         return 
#     if phone_number[5] != ' ':
#         return False
#     if phone_number[9] != '-':
#         return False
#     if not (phone_number[1:4].isdigit() and phone_number[6:9].isdigit() and phone_number[10:13].isdigit()):
#         return False
    
#     return True



# def is_int_array(arr):
#     if not arr:
#         return True
    
#     for element in arr:
#         if not isinstance(element, (int, float)) or (isinstance(element, float) and not element.is_integer()):
#             return False
    
#     return True



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



# def compute_sum(n):
#     sum = 0
    
#     for number in range(1, n + 1):
#         str_number = str(number)
#         if len(str_number) > 1:
#             for char in str_number:
#                 sum += int(char)
#         else:
#             sum += number


# def longestPalindrome(s):
#     if not s:
#         return 0
    
#     n = len(s)
#     dp = [[False] * n for _ in range(n)]
#     max_len = 1 
#     for i in range(n):
#         dp[i][i] = True
    

#     for i in range(n - 1):
#         if s[i] == s[i + 1]:
#             dp[i][i + 1] = True
#             max_len = 2
    
#     for length in range(3, n + 1): 
#         for i in range(n - length + 1):
#             j = i + length - 1
#             if s[i] == s[j] and dp[i + 1][j - 1]:
#                 dp[i][j] = True
#                 max_len = max(max_len, length)
    
#     return max_len
