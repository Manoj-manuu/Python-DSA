# # O(n*2)
# def firstNonRepeat(str):
#     for i in range(len(str)):
#         repeat = False
#         for j in range(len(str)):
#             if i != j and str[i]==str[j]:
#                 repeat = True
#         if repeat == False:
#             return i

# print(firstNonRepeat("abaRb150"))

#O(n)
def firstNonRepeat(strr):
    ht = {}
    for i in strr:
        if i in ht:
            ht[i]+= 1
        else:
            ht[i] = 1
    
    for i in range(len(strr)):
        if ht[strr[i]] == 1:
            return i

print(firstNonRepeat("abaRb150"))

print(firstNonRepeat("abRb150"))

