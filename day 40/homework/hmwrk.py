# def sum_digits(number):
#       abs_number = abs(number)
    
#       number_str = str(abs_number)
    
#       total_sum = 0
#       for char in number_str:

#         digit = int(char)
#         total_sum += digit
#         return total_sum

#     #ragac shecdoma maq arvici ra


# def solution(nums):
#     if nums is None or len(nums) == 0:
#         return []
    
#     return sorted(nums)



# def high(x):
#     def high(x):
#         words = x.split()
    
#     max_score = 0
#     max_word = ""
#     for word in words:
#         score = sum(ord(char) - ord('a') + 1 for char in word)
        
#         if score > max_score:
#             max_score = score
#             max_word = word
    
#     return max_word





# def find_missing_letter(chars):
    # for i in range(len(chars) - 1):
    #     if chars[i + 1] != chr(ord(chars[i]) + 1):