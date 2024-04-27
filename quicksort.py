from random import randint
def quicksort(arr):
	if len(arr) < 2: return arr
	p = arr[0]
	return quicksort(list(filter(lambda x: x<p, arr[1:]))) + list(filter(lambda x: x==p, arr[0:]))+ quicksort(list(filter(lambda x: x>p, arr[1:])))


my_list = []
for _ in range(100):
    my_list.append(randint(0,100))
print(my_list)
print(quicksort(my_list))