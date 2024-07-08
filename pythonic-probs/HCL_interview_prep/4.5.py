


def replace_tel_with_community(my_list):
    final_output = []
    for item in my_list:
        if item.endswith(".tel"):
            new_item = item.replace(".tel", ".community")
            final_output.append(new_item)
        else:
            final_output.append(item)

    
    return final_output

"""
 Doing it in-place instead of creating a new list
"""   

def replace_tel_with_community_in_place(my_list):
    for i in range(len(my_list)):
        if my_list[i].endswith(".tel"):
            my_list[i] = my_list[i].replace(".tel", ".community")

    return my_list

"""
Doing the same with list comprehension
"""

# my_list[:] = [item.replace(".tel", ".community") if item.endswith(".tel") else item for item in my_list]


# Drive Code
if __name__ == "__main__":
    my_list = ["snmp.tel", "snmprw.tel", "snmpro"]
    #print(replace_tel_with_community(my_list))
    #print(replace_tel_with_community_in_place(my_list))