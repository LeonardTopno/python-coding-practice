look_up = {
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000
}

def romans_to_int(s):
    n =  len(s) 
    integer = 0 # initializing integer

    i = n-1     # n-1 is the last index of the string

    while i >= 0: 
                                                            
        if i < n-1 and look_up[s[i]] < look_up[s[i+1]]:     # Handling Abnormal Case First # Case when former is later is larger than former - IV
            integer-=look_up[s[i]]
        else:                                               # Normal Case
            integer+=look_up[s[i]]
        
        i-=1
    
    return integer


# Driver Code
while(True):
    s = input("Enter the Roman Number:")
    print(romans_to_int(s))

'''
Things to learn:
i) order matters: when a lower value is after higher value: just add, else subtract
ii) Move backwards, as you will be able to figure out if you need to add or subtract


'''    