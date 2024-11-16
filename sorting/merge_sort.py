def mergeLists(lst1: list, lst2: list) -> list:
    """Merge two sorted lists into a single sorted list.
    Args:
        lst1: A sorted list of integers
        lst2: A sorted list of integers
    Returns:
        A sorted list of integers containing all the elements of lst1 and lst2
    """
    n1 = len(lst1)
    n2 = len(lst2)
    if n1 == 0:  # lst1 is empty
        return list(lst2)
    elif n2 == 0:
        return list(lst1)
    else:
        output_lst = []  # This is the list we will return
        i1 = 0
        i2 = 0
        while i1 < n1 or i2 < n2:
            if i1 < n1 and i2 < n2:  # We are processing both lists
                if lst1[i1] <= lst2[i2]:  # lst[i1] is the smaller elt
                    output_lst.append(lst1[i1])  # append to end of output list
                    i1 = i1 + 1  # advance index i1
                else:
                    output_lst.append(lst2[i2])  # append to end of output list
                    i2 = i2 + 1  # advance index i2
            elif i1 < n1:  # We have run past the end of lst2
                output_lst.append(lst1[i1])  # append lst1 to end of output list
                i1 = i1 + 1
            else:  # We have run past the end of lst1
                output_lst.append(lst2[i2])  # append lst2 to end of output list
                i2 = i2 + 1
        return output_lst

# helper function to swap the elements at two positions in the list
def swap(lst, i, j):
    n = len(lst)
    assert( i >= 0 and i < n)
    assert( j >= 0 and j < n)
    # We can use a simultaneous assignmment to swap
    (lst[i], lst[j]) = (lst[j], lst[i])
    return 

# this function copies the result of the merge back into the original list
# Function: copy_back
# output_lst is the list that contains right - left + 1 elements.
# lst is the list we need to copy into
# left and right are indices into list.
# TODO: copy elements from output_lst into lst[left:right+1]
# Note that python range left:right+1 includes indices from left,..., right.

def copy_back(output_lst, lst, left, right):
    # Ensure that the output has the right length for us to copy back
    assert(len(output_lst) == right - left + 1)
    for i in range(left, right+1):
        lst[i] = output_lst[i - left]
    return 

#Function: mergeHelper
# merge elements from lst[left:mid+1]  and lst[mid+1:right+1]
# create a temporary output list to hold the merged result and
# copy that back using the copy_back function.
# This was lst is modified in place. 
def mergeHelper(lst, left, mid, right):
    # Perform a merge on sublists lst[left:mid+1] and lst[mid+1:right+1]
    # This is the same algorithm as merge above but we will need to copy
    # things back to the original list.
    if left > mid or mid > right:  # one of the two sublists is empty
        return
    i1 = left
    i2 = mid + 1
    output_lst = []
    while (i1 <= mid or i2 <= right):
        if (i1 <= mid and i2 <= right):
            if lst[i1] <= lst[i2]:
                output_lst.append(lst[i1])
                i1 = i1 + 1
            else:
                output_lst.append(lst[i2])
                i2 = i2 + 1
        elif i1 <= mid:
            output_lst.append(lst[i1])
            i1 = i1 + 1
        else:
            output_lst.append(lst[i2])
            i2 = i2 + 1
    copy_back(output_lst, lst, left, right)
    return 
# Function: mergeSortHelper
# recursive implementation of mergesort.
def mergesortHelper(lst, left, right):
    # worst case time complexity: O(n log n)
    # analysis:
    # let T(n) be the time complexity of the merge sort algorithm
    # T(n) = 2T(n/2) + O(n)
    # T(n) = 2(2T(n/4) + O(n/2)) + O(n) # expand the first term
    # T(n) = 4T(n/4) + 2O(n) + O(n) # expand the second term
    # ... carry on until we get to the base case
    # i.e. n = 2^k i.e k = log n times
    # T(n) = nT(1) + O(n log n) = O(n log n)
    # this is specialized case of the general master theorem
    # for divide and conquer algorithms.
    # T(n) = aT(n/b) + f(n) where a = 2, b = 2, f(n) = O(n)
    if (left == right): # Region to sort is just a singleton
        return 
    elif (left + 1 == right): # region to sort has two elements
        if (lst[left] > lst[right]): # compare 
            swap(lst, left, right)   # and swap if needed
    else: 
        mid = (left + right ) // 2  # compute mid point. 
        # Note that // is integer division in python3.
        mergesortHelper(lst, left, mid) # Sort left half recursively
        mergesortHelper(lst, mid + 1 , right) # Sort right half recursively
        mergeHelper(lst, left, mid, right) # merge them together.
        
# Function mergesort
#   Sort the list in place and modify it so that 
#   lst is sorted when the function returns.
def mergesort(lst):
    if len(lst) <= 1:
        return # nothing to do
    else:
        # recursively call the helper function
        mergesortHelper(lst, 0, len(lst)-1)

if __name__ == "__main__":
    lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print("Before sorting: ", lst)
    mergesort(lst)
    print("After sorting: ", lst)
    assert(lst == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])
    print("All tests pass")
        