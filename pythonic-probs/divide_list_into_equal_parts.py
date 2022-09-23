"""
generator example
"""

def getChunks(lst, chunk_size):
    for i in range(0, len(lst), chunk_size):
        yield lst[i : i+chunk_size]

#Drive code:
#import pprint
lst = [0,1,2,3,4,5,6,7,8,9,10]
#pprint.pprint(list(getChunks(lst, 3)))   #<generator object getChunks at 0x7f9b8bd08d60>, so convert into list
print(list(getChunks(lst, 3)))   #<generator object getChunks at 0x7f9b8bd08d60>, so convert into list