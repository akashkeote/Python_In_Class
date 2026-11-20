nums=[4,2,9,7,5,1,6,8]

even=[]
for i in nums:
    if i%2==0:
        even.append(i)
print(even)

#now using filter in one line
even = list(filter(lambda n:n%2==0,nums))
print(even)

#3rd problem
listt=[55,698,34,56]
print(list(filter(lambda n:n>50,listt)))

