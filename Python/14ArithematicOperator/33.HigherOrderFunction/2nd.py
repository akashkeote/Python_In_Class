def operate(nums,operations):
    for i in nums:
        res=operations(i)
        print(res)

def sq(n):
    return n*n
list = [1,2,3,4,5,6]
operate(list,sq)