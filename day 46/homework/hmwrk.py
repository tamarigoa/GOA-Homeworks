# def reverse_bits(n):
#     reversed_num = 0
#     while n > 0:
#         reversed_num = reversed_num << 1
#         reversed_num |= (n & 1)
#         n >>= 1
#     return reversed_num

def spot_diff(s1, s2):
    return [i for i in range(len(s1)) if s1[i] != s2[i]]