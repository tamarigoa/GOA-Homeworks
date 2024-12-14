# def sentence_words(sentence):
#     word=sentence.split(" ")
#     return ", ".join(word)


# print(sentence_words("Hello World"))



# შექმენით ფუნქცია, რომელიც მიიღებს წინადადებას და დაბეჭდავს მის თითოეულ სიტყვაში სიმბოლოების რაოდენობას(ცალ-ცალკე)
# def word(st):
#     words=st.split(" ")
#     for word in words:
#         print(len(word))
# word("Goa is the best")



# შექმენით ფუნქცია, რომელიც იღებს წინადადებას, სადაც ყოველი სიტყვის შორის ერთზე მეტი დაშორებაა(space). თქვენი დავალებაა ჩამოაშოროთ გადმოცემულ წინადადებას ზედმეტი space-ები(სიტყვებს შორის მხოლოდ ერთი უნდა იყოს). საბოლოოდ დააბრუნეთ ეს წინადადება

# def remove_spaces(st):
#     st=st.split(" ")
#     list=[]
#     for i in st:
#         if i !="":
#             list.append(i)
#     return " ".join(list)

# print(remove_spaces("Hi    my  name    is    luka"))





# შექმენით ფუნქცია, რომელიც იღებს წინადადებას, და მასში space-ების მაგივრად სიტყვებს შორის ჩასვამს ტირეს("-"). საბოლოოდ კი აბრუნებს მას

# def replace(st):
#     st=st.split(" ")
#     list=[]
#     for i in st:
#         list.append(i)
#     return "-".join(list)
# print(replace("Hello World i am new"))


#  შექმენით ფუნქცია, რომელსაც გადაეცემა წინადადება. თქვენი დავალებაა ამ წინადადების სიტყვები შეაბრუნოთ და დააბრუნოთ(სიტყვების სიმბოლოები არ უნდა იყოს შებრუნებული)

# მაგალითად: "Hello World!" >>> "World! Hello"

# def reverse(st):
#     st=st.split(" ")
#     return " ".join (st[::-1])
# print(reverse("Hello world"))