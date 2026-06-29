def uniqueSubset(str):
    maxLen = 0
    start = 0
    seen = {}
    for i in range(len(str)):
        ch = str[i]
        if ch in seen:
            start = max(start,seen[ch]+1)
        maxLen =  max(maxLen, i - start + 1)
        seen[ch] = i
    
    return maxLen

print(uniqueSubset(""))