# def capitals(word):
#     list = []
#     for i, char in enumerate(word):
#         if char.isupper():
#             list.append(i)
    
#     return list

# def vaporcode(s):
#     s=s.upper()
#     l=[]
#     s=s.replace(" ","")
#     for i in s:
#         l.append(i)
#     return "  ".join(l)

# def nb_dig(n, d):
#     l=[]
#     count=0
#     for i in range(0,n+1):
#         l.append(str(i**2))
#     for i in l:
#         for x in i:
#             if str(d)==x:
#                 count+=1
#     return count        

# def divisors(n):
#     count=0
#     for i in range(1,n+1):
#         if n % i==0:
#             count+=1
#     return count


# def number(bus_stops):
#     people = 0  
    
#     for get_on, get_off in bus_stops:
#         people += get_on  
#         people -= get_off
#     return people

# def count_bits(n):
#     x=bin(n)
#     count=0
#     x=x[2:]
#     for i in x:
#         if i=="1":
#             count+=1
#     return count

# def digital_root(n):
#     n=str(n)
#     sum=0
#     for i in n:
#         sum+=int(i)
#         if len(str(sum))>1:
#             sum=int(str(sum)[0]) + int(str(sum)[-1])
#     return sum


# def spin_words(st):
#     st=st.split(" ")
#     result=[]
    
#     for i in st:
#         if len(i)>=5:
#             result.append(i[::-1])
#         else:
#             result.append(i)
#     return " ".join (result)


