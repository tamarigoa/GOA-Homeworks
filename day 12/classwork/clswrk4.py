numbers=[1,2,3,4,5,6,7,8,9,10]
numbers2=[]

for i in numbers:
    if i % 2 ==0:
        numbers2.append(i)


print(numbers2)



sum=0

for number in numbers2:
    sum += number

print(sum//len(numbers2))