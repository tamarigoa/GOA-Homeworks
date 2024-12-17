# def hero(bullets, dragons):
#      return bullets >= dragons * 2

# def reverse_number(num):
#     num=str(num) 
#     num=num[::-1]
    
#     if num.endswith("-"):
#         num=num[:-1]
#         num="-"+num
#     return int(num)



# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result


# def remove_url_anchor(url):
#     if '#' in url:
#         return url.split('#')[0]
#     return url



# def kebabize(n):
#     st=""
#     for i in n:
#         if i.isalpha():
#             if i.isupper():
#                 st+="-"+i.lower()
#             else:
#                 st+=i
#     if len(st)>0:
#         if st[0]=="-":
#             st=st[1:]
#     return st