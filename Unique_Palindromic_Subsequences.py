# 1930. Unique Length-3 Palindromic Subsequences
def countPalindromicSubsequence(s):
    count = 0

    for l in set(s):
        i,j = s.find(l),s.rfind(l)
        if j>i+1:
            count += len(set(s[i+1:j]))
    return count


if __name__ =='__main__':
    s = "acb"
    print(countPalindromicSubsequence(s))
