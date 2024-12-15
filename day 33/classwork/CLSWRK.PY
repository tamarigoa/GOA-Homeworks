# def manual_join(str_list, string1):
#     result = ""

#     for i in str_list:
#         result += i + string1
#     return result[:-3]


# print(manual_join(list("Python"), " - "))




# str=input("Enter your string")
# index=0
# for i in str:
#     print(i+"-",str(index))
#     index+=1



# def manual_count(collection, element):
#     count = 0
#      for item in collection:
#        if item == element:
#              count += 1
#    return count

# my_list = [1, 2, 3, 2, 4, 2]
# my_string = "hello world"

# print(manual_count(my_list, 2))  

# print(manual_count(my_string, 'o'))  







# def manual_replace(text):
#     # აქ შეინახება შედეგი
#     result = ""
    
#     for char in text:
#         if char == ' ':
#             # თუ სიმბოლო არის დაშორებით შეცვალე ტირეთი
#             result += '-'
#         else:
#             # თუ არაა უბრალოდ დაამატოს
#             result += char
    
#     #ვაბრუბნბ ახალ სთრინგს
#     return result
# text = "Hello world, how are you?"
# new_text = manual_replace(text)
# print(new_text)
