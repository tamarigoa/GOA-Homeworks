# def reverse_it(data):
#     if type(data) == str:
#         return data[::-1]
#     elif type(data) == int:
#         return int(str(data)[::-1])
#     elif type(data) == float:
#         return float(str(data)[::-1])
#     return data

# def shared_bits(a, b):
#     count = 0
    
#     while a > 0 or b > 0:
#         if (a & 1) and (b & 1):
#             count += 1
#             if count >= 2: 
#                 return True
        
#         a >>= 1
#         b >>= 1
    
#     return False



# def freq_seq(s, sep):
#     char_count = {char: s.count(char) for char in s}
#     translated = [str(char_count[char]) for char in s]
#     return sep.join(translated)

# def find_missing_numbers(arr):
#     missing_numbers = []
#     for num in range(arr[0], arr[-1] + 1):
#         if num not in arr:
#             missing_numbers.append(num)
#     return missing_numbers
