list=[100,200,300,400,500,600,700]
print(list[-1:-3])
print(list[1:4:3])# cannot give negative indexing in slicing
# 1 is stating index, 4 is stop value,3 is skip value
print(list[-4:-3:2])

list=[2,6,8,3,9]
list.reverse()
print(list)
list.append(10)
print(list) 
list.insert(2,15)
print(list) 
list.remove(3)
print(list)     
list.sort()
print(list)
