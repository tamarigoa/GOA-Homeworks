# def find_short(s):
#     words = s.split()
#     shortest_length = min(len(word) for word in words)
#     return shortest_length



# def is_isogram(string):
    
#     st_low = string.lower()
#     if string == "":
#         return True
#     for i in st_low :
#         if st_low.count(i) >= 2:
#             return False
#     return True





# def validate_pin(pin):
#     return len(pin) in [4, 6] and pin.isdigit()

# def xo(s):
#     s = s.lower()
    
#     count_x = s.count('x')
#     count_o = s.count('o')
#     return count_x == count_o

# def to_camel_case(text):
#     st = ""
#     s = ""
#     for i in text:
#         if i == "_" or i == "-":
#             st += i.replace(i," ")
#         else:
#             st += i
#     st = st.split(" ")
#     for i in range(len(st)):
#         if i >= 1:
#             s += st[i].capitalize()
#         elif i == 0:
#             s += st[i]
#     return s



# def longest(a1, a2):
#     mixed = list(a1) + list(a2)
#     return "".join(sorted(set(mixed)))
