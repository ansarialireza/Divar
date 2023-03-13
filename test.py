import Sql

list=[[0,1,2,3],[0,1,2,3,4,5],[0,1,2,3],[0,1,2,3],[0,1,2,3],[0,1,2,3,4]]
for i in list:
    if len(i) != 4:
        list.remove(i)
print(list)