def lcs(text1, text2):

    print("text1", text1)
    print("text2", text2)

    len_text1, len_text2 = len(text1), len(text2)

    if len_text1 == 0 or len_text2 == 0:
            return 0

    lcs = [0 for x in range(len_text2+1)] #storing numbers in list which will be used to count

    print("Original lcs initialized:", lcs)
    print("****** Begins ******")
    for elem in text1:

        lcs_temp = [0]
        print("-------------------------", elem)
        print("LCS at this point", lcs)
        print("lcs_temp:", lcs_temp)

        for index, item in enumerate(text2): # index starts with 0, every element in text1 is compared to elem in text2
            if elem == item:
                print(lcs_temp, end=" ")
                lcs_temp.append(lcs[index]+1) # Whatever value is there at index of lcs + 1 
                print("lcs_temp match ---- ",item ,": ",  lcs_temp)
            else:
                print("\n", lcs_temp[-1], lcs[index+1])
                print(lcs_temp, end=" ")
                lcs_temp.append(max(lcs_temp[-1], lcs[index+1])) #last element of lcs_temp vs next element of lcs(intitially 0 though). Which ever is bigger 
                print("lcs_temp MISMATCH ----", item, ": ",  lcs_temp)
        lcs = lcs_temp
        print("lcs:", lcs)
    
    print("\n ********** Done *************")
    print("lcs: ", lcs_temp)
    return lcs[-1] 

#driver code
x="AC"
y="ABC"

lcs_ = lcs(x,y)
print(lcs_)
