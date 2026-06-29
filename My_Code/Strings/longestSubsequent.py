def longest_subsequnet(strr):
    start = 0
    max_len = 0
    seen = {}
    for i in range(len(strr)):
        char = strr[i]
        if char in seen:
            start = max(start,seen[char]+1)
        max_len = max(max_len,i - start + 1)
        seen[char] = i
    return max_len

print(longest_subsequnet("pqbrstbuvwvxy"))