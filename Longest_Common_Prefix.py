def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    strs.sort()
    first_word = strs[0]
    last_word = strs[-1]
    length = min(len(first_word), len(last_word))
    i = 0
    
    while i < length and first_word[i] == last_word[i]:
        i += 1

    return first_word[:i]


    

if __name__ == '__main__':
    strs =["flower","flow","flight"]
    print(longestCommonPrefix(strs))