# def dup(arry):
#     result = []
    
#     for word in arry:
#         changed_word = word[0]
#         for i in range(1, len(word)):
#             if word[i] != word[i-1]:
#                 changed_word += word[i]
#         result.append(changed_word)
        
#     return result

# vowels = ["a", "e", "i", "o", "u"]

# def encode(st):
#     result = ""

#     for char in st:
#         if char in vowels:
#             result += str(vowels.index(char) + 1)
#         else:
#             result += char
    
#     return result

# encoded_str = encode("Hello World")
    
    
# def decode(st):
#     result = ""

#     for char in st:
#         if char.isdigit():
#             result += vowels[int(char) - 1]
#         else:
#             result += char
    
#     return result