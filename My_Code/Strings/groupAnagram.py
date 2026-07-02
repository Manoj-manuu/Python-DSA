def group_anagram(strr):
    if len == 0:
        return []
    sorted_string = [''.join(sorted(i)) for i in strr]
    seen = {}
    for i in range(len(sorted_string)):
        if sorted_string[i] in seen:
            seen[sorted_string[i]].append(strr[i])
        else:
            seen[sorted_string[i]] = [strr[i]]
    return list(seen.values())
    
print(group_anagram(['arc','abc','car','cat','act','acb','atc']))