# Lambda Functions - Important Notes

# Lambda function ka syntax:
# lambda arguments: expression

# Important points:
# - Lambda one-line function hota hai.
# - Lambda zero, one ya multiple arguments le sakta hai.
# - Lambda mein ek hi expression hota hai.
# - Expression ka result automatically return hota hai.
# - Lambda ka use map(), filter() aur sorted() ke saath common hai.
# - Lambda anonymous hota hai, lekin use variable mein store kar sakte hain.
# - Lambda mein statements, multiple lines ya normal block logic nahi likhte.
# - Complex logic ke liye def function zyada readable hota hai.

# Lambda recursion ke liye suitable nahi hota.
# Readability ke liye simple kaam mein lambda use karo.
# Reusable ya complex kaam ke liye def use karo.

from numpy import sqrt

x1=[1,4,9,16,25]
print(list(map(sqrt,map(sqrt,x1))))
print(list(map(lambda n:n**0.5,x1)))
x2=list(range(10))
print(x2)
# map job to work on the output collects outputs 
# and filter job is work on input
# filter me true and false vale hi values dene chahiye hame
print(list(filter(lambda n:n%2==0,x2)))
print(list(filter(lambda n:n*n,x2)))
print(filter(lambda n : n%2==0,x2))
print(list(map(lambda n:n**0.5,filter(lambda n:n%2==0,x2))))
m=123
print(str(m))
print(list(str(m)))
print(list(map(int,str(m))))

print(sum(map(lambda n:n*n*n,map(int,str(m)))))
print(sum(map(lambda n:n*n*n,map(int,str(m))))==m)
print(filter(lambda m:sum(map(lambda n:n*n*n,map(int,list(str(m)))))(123)))
print(filter(lambda m:sum(map(lambda n:n*n*n,map(int,list(str(m)))))==m,range(1000)))
print(filter(lambda m:sum(map(lambda n:n*n*n,map(int,list(str(m)))))==m,range(10000)))

print(i|0<i<100,i mod 2==0)
print(i for i in range(100) if i%2==0)
#yaha i aur j is list of tuples
print(i,j for i in range(100) for j in range(100) if i%2==0 and j%2==0)
print(i,j,k for i in range(1,10,2) for j in range(1,10,2) for k in range(1,10,2) if i%2==0 and j%2==0 and k%2==0)
print([i*i for i in range(10)])
print( i for i in range(1,m//2+1)IF m%i==0)
m=11
print(i for i in range(1,m//2+1) if m%i==0)
m=13
print(i for i in range(1,m//2+1) if m%i==0)
print(len([i for i in range(1,m//2+1) if m%i==0])==1)
print(list(filter(lambda m:len([i for i in range(1,m//2+1) if m%i==0])==1,range(1,1000))))
