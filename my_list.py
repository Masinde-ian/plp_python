my_list = []
a=10
i=1
while i <= 4:
    my_list.append(a)
    a +=10
    i +=1
print('The initial list:',my_list)
my_list.insert(1,15)
print('List after inserting 15 as the 2nd term:',my_list)
another_list = [50,60,70]
my_list.extend(another_list)
print('The extended list:',my_list)
my_list.pop()
print('The list after removing the last item:',my_list)
my_list.sort()
print('The list sorted in ascending order:',my_list)
print('The index of 30 is ',my_list.index(30))
