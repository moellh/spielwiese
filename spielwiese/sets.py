

def sets_over_k(n,k,start=0):
    '''
    Returns sets of length k with elements from 1 to n, starting from start.

    Parameters
    ----------
    n : int:

    k : int

    start : int = 0

    Returns
    -------
    generator of sets
    '''

    if k==1:
        for j in range(start,n+1):
            yield {j}
    else:
        for i in range(start,n-k+2): # start to n-k+1 (last element to allow set of length k)
            for s in sets_over_k(n,k-1,i+1):
                yield {i}.union(s)
