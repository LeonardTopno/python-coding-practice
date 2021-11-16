def getNthFibNum(n):
    '''
    Returns n-th number in Fibonacci Sequence
    '''
    if n <=1 :
        return n

    return (getNthFibNum(n-1) + getNthFibNum(n-2))


# driver code
'''
Takes num of terms - nterm prints the Fibonacci Series of nterms in list format
'''
while (True):
    nterm = int(input("\n Enter the number of terms in the Fibonacci Series: "))

    if nterm <= 0:
        nterm=int(input("Please enter a valid num ( >= 1): "))

    fibSeq = [] # declaring an empty list to store Fibonacci Series
    for term in range(nterm):
        fibSeq.append(getNthFibNum(term))
    
    print("Fibonacci Sequence upto", nterm, "terms :", fibSeq)

#------------------------------- Problem Statement --------------------------------------
'''
Write a Program to display Fibonacci Sequence/Series upto n-th terms 
'''