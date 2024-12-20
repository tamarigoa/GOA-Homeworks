# def collatz(n):
#     steps = 1 
#     while n != 1:
#         if n % 2 == 0: 
#             n = n // 2
#         else: 
#             n = 3 * n + 1
#         steps += 1 
#     return steps


# def most_frequent_count(arr):
#     if not arr:
#         return 0
#     n = {}
#     for num in arr:
#         if num in n:
#             n[num] += 1
#         else:
#             n[num] = 1

#     max_count = max(n.values())

#     return max_count