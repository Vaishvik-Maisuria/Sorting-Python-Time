def descending_selection_sort(L):
	'''(List) -> None type
	
	The function descending_selection_sort mutates the list L and sorts it in non-ascending, rather than non-descending order.
	
	
	
	
	>>>descending_selection_sort([5,3,7])
	[7, 5, 3]
	>>> descending_selection_sort([7])
	[7]
	>>> descending_selection_sort([])
	[]
	'''
	
	i = 0
	
	while i < len(L):
		index_min = i
		index = i + 1
		while index < len(L):
			if L[index] > L[index_min]:
				index_min = index
			index += 1		
		min_index = index_min
		L[min_index], L[i] = L[i], L[min_index]
		i += 1	

	print(L)
	      

def backwards_insertion_sort(L):
	''' (List) -> None Type
	
	
	the function backwards_insertion_sort mutates the list L and sorts it working backwards from the end of the list.
	
	>>> backwards_insertion_sort([])
	[]
	>>> backwards_insertion_sort([1,9,3,8,4])
	[1,3,4,8,9]
	>>> backwards_insertion_sort([9])
	[9]
	'''
	
	for i in range(len(L)-1, -1, -1):
		for j in range( i +1, len(L)):
			if L[j-1] > L[j]:
				L[j-1], L[j] = L[j], L[j-1]
	
	
	print(L)

		
	 #   insert L[i] where it belongs in L[0 : i + 1]
	
	
def Gnome_Sort(L):
	'''
	
	
	
	
	'''


'''
L is a list to be sorted
  set index to 0 and next_index to 1
  while index isn’t referring to the last item in the list
    compare the items in L at index and index + 1
    if the items in L at index and index + 1 are in sorted (non-descending) order
       set index to next_index
       increment next_index
    else
       swap the items
       decrement index (but don’t decrement index below 0)
  L is sorted

'''




def make_list(n):
	'''(int) -> list of int
	
	Return a random list of n ints.
	'''
	
	import random
	res = list(range(n))
	random.shuffle(res)
	return res

def time_listfunc(f, n, m):
	'''(func, int, int) -> float
	
	Return how many seconds it takes to run function f on a shuffled 
	list with n items, on average over m times.
	'''

	import time
	total = 0
	for i in range(m):
		L = make_list(n)
		t1 = time.time()
		L = f(L)
		t2 = time.time()
		total += t2 - t1
	return total / m