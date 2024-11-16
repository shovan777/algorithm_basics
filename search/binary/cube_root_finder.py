def integerCubeRootHelper(n, left, right):
    # Time complexity: O(log n)
    # Analysis same as binary search
    cube = lambda x: x * x * x # anonymous function to cube a number
    assert(n >= 1)
    assert(left < right)
    assert(left >= 0)
    assert(right < n)
    assert(cube(left) < n), f'{left}, {right}'
    assert(cube(right) > n), f'{left}, {right}'
    # your code here
    # first lets find mid index
    mid = (left + right) // 2
    
    # check if mid is goal
    if cube(mid+1) > n:
        if cube(mid) <= n:
            # voila found
            return mid
        return integerCubeRootHelper(n, left, mid)
    return integerCubeRootHelper(n, mid, right)
    
    
# Write down the main function
def integerCubeRoot(n):
    assert( n > 0)
    if (n == 1): 
        return 1
    if (n == 2):
        return 1
    return integerCubeRootHelper(n, 0, n-1)

if __name__ == "__main__":
    assert(integerCubeRoot(1) == 1)
    assert(integerCubeRoot(2) == 1)
    assert(integerCubeRoot(4) == 1)
    assert(integerCubeRoot(7) == 1)
    assert(integerCubeRoot(8) == 2)
    assert(integerCubeRoot(20) == 2)
    assert(integerCubeRoot(26) == 2)
    for j in range(27, 64):
        assert(integerCubeRoot(j) == 3)
    for j in range(64,125):
        assert(integerCubeRoot(j) == 4)
    for j in range(125, 216):
        assert(integerCubeRoot(j) == 5)
    for j in range(216, 343):
        assert(integerCubeRoot(j) == 6)
    for j in range(343, 512):
        assert(integerCubeRoot(j) == 7)
    print('Congrats: All tests passed! (10 points)')