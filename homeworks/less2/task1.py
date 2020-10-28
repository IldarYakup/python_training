my_list = [2, 'text', 456, 45.3, None, [1, 2, 3], {1, 2, 3}]
my_list.reverse()
n = len(my_list)
while n > 0:
    print(my_list[n-1], type(my_list[n-1]))
    n-=1
