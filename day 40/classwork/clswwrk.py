# def reverse_bits(n):
#     reversed_num = 0
#     while n > 0:
#         reversed_num = reversed_num << 1
#         reversed_num |= (n & 1)
#         n >>= 1
#     return reversed_num





# def move_zeros(lst):
#     def move_zeros(lst):
#         non_zero = 0
#         for i in range(len(lst)):
#             if lst[i] != 0:
#                 lst[non_zero] = lst[i]
#             non_zero_index += 1
    
#     for i in range(non_zero, len(lst)):
#         lst[i] = 0
    
#     return lst