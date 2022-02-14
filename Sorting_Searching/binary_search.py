
def iterative_binary_search(a, key):
	low = 0
	high = len(a)-1
	while(low <= high):
		mid = (low + high)//2
		if a[mid] == key:
			return mid

		elif key > a[mid]:
			low = mid + 1

		else:
			high = mid - 1

	return -1


def recursive_binary_search(a, key, low, high):
	if low > high:
		return -1

	mid_index = (low + high)//2

	if a[mid_index] == key:
		return mid_index

	if key > a[mid_index]:
		return recursive_binary_search(a, key, mid_index + 1, high)

	
	return recursive_binary_search(a, key, low , mid_index - 1)


a = [-4, -1, 3, 7, 10, 11]
index = iterative_binary_search(a, 7)
index_ = recursive_binary_search(a, 7, 0, len(a)-1)

print('Iterative_index_found', index)
print('Recursive_index_found', index_)