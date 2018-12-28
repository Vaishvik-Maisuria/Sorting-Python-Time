############### Bubble Sort ###############        

def bubble_sort(L):
    '''(list) -> NoneType
    Sort the items in L in non-descending order.

    >>> L = [1, 4, 2, 5, 3, 6]
    >>> bubble_sort(L)
    >>> L
    [1, 2, 3, 4, 5, 6]
    '''
    
    uns_index = len(L) - 1
    while uns_index > 0:
        for curr_index in range(uns_index):
            if L[curr_index] > L[curr_index + 1]:
                L[curr_index], L[curr_index + 1] = L[curr_index + 1], L[curr_index]        
        uns_index -= 1
    

############### Selection Sort ###############        

def find_minimum(L, start_index):
    '''() -> int
    Return the index of the smallest value in the list that occurs at or after
    start_index.
    Note: start_index must be legal, so L cannot be empty.
    
    >>> find_minimum([5, 3, 7, 4], 0)
    1
    >>> find_minimum([3, 5, 7, 4], 1)
    3
    '''
    index_min = start_index
    index = start_index + 1
    while index < len(L):
        if L[index] < L[index_min]:
            index_min = index
        index += 1
    return index_min
    

def selection_sort(L):
    '''(list) -> NoneType
    Sort the items in L in non-descending order.
    >>> L = [5, 3, 7, 4]
    >>> selection_sort(L)
    >>> L
    [3, 4, 5, 7]
    
    >>> L = [1, 4, 2, 5, 3, 6]
    >>> selection_sort(L)
    >>> L
    [1, 2, 3, 4, 5, 6]
    '''
    
    uns_index = 0
    while uns_index < len(L):
        min_index = find_minimum(L, uns_index)
        L[min_index], L[uns_index] = L[uns_index], L[min_index]
        uns_index += 1


############### Insertion Sort ###############        

def insert(L, index):
    '''(list, int) -> NoneType
    Insert the item at position index in list L into the range
    [0..index] so that [0..index] is sorted. [0..index-1] is 
    already sorted.
    
    >>> L = [1, 0]
    >>> insert(L, 1)
    >>> L
    [0, 1]
    '''
    
    while index > 0 and L[index - 1] > L[index]:
        L[index], L[index - 1] = L[index - 1], L[index]
        index -= 1
    

def insertion_sort(L):
    '''(list) -> NoneType
    Sort the items in L in non-descending order.
    >>> L = [5, 3, 7, 4]
    >>> insertion_sort(L)
    >>> L
    [3, 4, 5, 7]
    
    >>> L = [1, 4, 2, 5, 3, 6]
    >>> insertion_sort(L)
    >>> L
    [1, 2, 3, 4, 5, 6]
    '''
    
    uns_index = 1
    while uns_index < len(L):
        insert(L, uns_index)
        uns_index += 1
        

############### Insertion Sort ###############

def system_sort(L):
    '''A wrapper for the system's sort function, so we can time it.
    '''
    L.sort()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
    
    from timing import time_listfunc
    print("bubble 4000", time_listfunc(bubble_sort, 4000, 3))
    print("selection 4000", time_listfunc(selection_sort, 4000, 3))
    print("insertion 4000", time_listfunc(insertion_sort, 4000, 3))
    print("system sort 4000", time_listfunc(system_sort, 4000, 3))
    