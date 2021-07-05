def lcs_fun(text1, text2):
    len_text1, len_text2 = len(text1), len(text2)

    lcs = [0 for i in (range(len_text2+1))]

    for elem in text1:
        lcs_temp = [0]

        for index, item in enumerate(text1):
            if elem == item:
                lcs_temp.append(lcs[index]+1)
            else:
                lcs_temp.append(max(lcs_temp[-1], lcs[index+1]))

        lcs = lcs_temp

    return lcs[-1]

#driver program
text1="ABC"
text2="BC"

result=lcs_fun(text1,text2)
print(result)



