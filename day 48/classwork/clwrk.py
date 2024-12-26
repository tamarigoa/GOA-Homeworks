# def in_asc_order(arr):
#     if len(arr) <= 1:
#         return True
#     for i in range(len(arr) - 1):
#         if arr[i] > arr[i + 1]:
#             return False
    
#     return True 


# # return masked string
# def maskify(cc):
#     if len(cc) <= 4:
#         return cc

#     return "#" * (len(cc) - 4) + cc[-4:]








# def valid_braces(string):
#     brace = {'(': ')', '[': ']', '{': '}'}
#     stack = []

#     for char in string:
#         if char in brace:  
#             stack.append(char)
#         else:
#             if not stack or brace[stack.pop()] != char:
#                 return False

#     return not stack





# def expanded_form(num):
#     num_str = str(num) 
#     length = len(num_str)
#     expand=[]

#     for i, digit in enumerate(num_str):
#         if digit != '0': 
#             expand.append(digit + '0' * (length - i - 1))

#     return ' + '.join(expand)