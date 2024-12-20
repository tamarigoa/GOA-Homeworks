# def check_exam(arr1,arr2):
#     count=0
#     for i in range(len(arr1)):
#         if arr1[i]==arr2[i]:
#             count+=4
#         if arr2[i] =="":
#             count+=0
#         elif arr1[i]!=arr2[i]:
#             count-=1
#     if count<=0:
#         return 0
#     else:
#         return count


# def backwards_prime(start, stop):
#     backwards_primes = []
    
#     for num in range(start, stop + 1):
#         if is_prime(num):
#             reversed_num = int(str(num)[::-1])
#             if reversed_num != num and is_prime(reversed_num):
#                 backwards_primes.append(num)
    
#     return backwards_primes