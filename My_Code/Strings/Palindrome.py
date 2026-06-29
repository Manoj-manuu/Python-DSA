def palindromee(strr):
    i = 0 
    j = len(strr) - 1
    if str == "":
        return True
    while(i<j):
        if strr[i]!=strr[j]:
            return False
        i +=1
        j-= 1
    return True
        

print(palindromee("ab"))

# def palindromee(strr):
#     new_str = ""
#     for i in reversed(range(len(strr))):
#         new_str += strr[i]
    
#     if new_str == strr:
#         return True
#     return False

# print(palindromee("aab"))
