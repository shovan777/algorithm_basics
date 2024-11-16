def twoWayMerge(lst1, lst2):
    # Time complexity: O(n+m) where n is the length of lst1 and m is the length of lst2
    # Analysis
    # ---------

    # Implement the two way merge algorithm on 
    #          two ascending order sorted lists
    # return a fresh ascending order sorted list that 
    #          merges lst1 and lst2
    # your code here
    pt1, pt2 = 0,0
    merged_list = []
    len_merged_list = len(lst1) + len(lst2)
    while (pt1 < len(lst1)) and (pt2 < len(lst2)):
        if lst1[pt1] <= lst2[pt2]:
            merged_list.append(lst1[pt1])
            pt1 += 1
        else:
            merged_list.append(lst2[pt2])
            pt2 += 1
    if pt1 < len(lst1):
        merged_list.extend(lst1[pt1:])
    if pt2 < len(lst2):
        merged_list.extend(lst2[pt2:])
    return merged_list
    
# given a list_of_lists as input, 
#   if list_of_lists has 2 or more lists, 
#        compute 2 way merge on elements i, i+1 for i = 0, 2, ...
#   return new list of lists after the merge
#   Handle the case when the list size is odd carefully.
def oneStepKWayMerge(list_of_lists):
    # Time complexity: O(n*k^2) where n is the total number of elements in all the lists
    # and k is the number of lists in list_of_lists
    # Analysis
    # the running time of two way merge is $\theta(n+m)$

    # now, we perform this k times so the total run time is

    # first we have 
    # list is empty first so

    # ((n+n))= 2n we do this at 1 step

    # 2n + n = 3n at 2 step

    # ...

    # (k-1)n at k step

    # n(2+3+..+k-1) = $\theta(n*(k^`2-1))$ = O(n*k^2)
    if (len(list_of_lists) <= 1):
        return list_of_lists
    ret_list_of_lists = []
    k = len(list_of_lists)
    for i in range(0, k, 2):
        if (i < k-1):
            ret_list_of_lists.append(twoWayMerge(list_of_lists[i], list_of_lists[i+1]))
        else: 
            ret_list_of_lists.append(list_of_lists[k-1])
    return ret_list_of_lists
    
# Given a list of lists wherein each 
#    element of list_of_lists is sorted in ascending order,
# use the oneStepKWayMerge function repeatedly to merge them.
# Return a single merged list that is sorted in ascending order.
def kWayMerge(list_of_lists):
    # Time complexity: O(n k^2 log k) where n is the total number of elements in all the lists
    # and k is the number of lists in list_of_lists
    # Analysis
    # the running time of oneStepKWayMerge is O(n*k^2)
    # we can see that the number of lists in the list of lists is halved at each step
    # until we have only one list left at last recursion
    # so the total number of steps is log k
    # so the total running time is O(n k^2 log k)
    k = len(list_of_lists)
    if k == 1:
        return list_of_lists[0]
    else:
        new_list_of_lists = oneStepKWayMerge(list_of_lists)
        return kWayMerge(new_list_of_lists)


if __name__ == "__main__":
    # BEGIN TESTS
    lst1= kWayMerge([[1,2,3], [4,5,7],[-2,0,6],[5]])
    assert lst1 == [-2, 0, 1, 2, 3, 4, 5, 5, 6, 7], "Test 1 failed"

    lst2 = kWayMerge([[-2, 4, 5 , 8], [0, 1, 2], [-1, 3,6,7]])
    assert lst2 == [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8], "Test 2 failed"

    lst3 = kWayMerge([[-1, 1, 2, 3, 4, 5]])
    assert lst3 == [-1, 1, 2, 3, 4, 5], "Test 3 Failed"

    print('All Tests Passed = 15 points')
    #END TESTS