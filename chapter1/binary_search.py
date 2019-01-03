#示例：猜数字游戏，使用二分法查找目标数字。

#!/usr/bin/python
def binary_search(mylist,item):
    low = 0
    high = len(mylist)-1
    
    while low <= high:                        #保证列表元素大于一个
        mid = (low + high) // 2               #取列表中间元素的索引，"//"取整数部分
        guess = mylist[mid]                   
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
            
        else:
            low = mid + 1
            
    return None                              #若元素不在列表中则返回None

mylist = [1,3,5,7,9]

print ("location of item is :",binary_search(mylist,4))
print (binary_search(mylist,1))
