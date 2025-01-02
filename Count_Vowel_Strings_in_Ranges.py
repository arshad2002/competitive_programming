# 2559. Count Vowel Strings in Ranges

def vowelStrings(words, queries):
    vowel = set('aeiou')
    result = []
    words_len = len(words)
    prefix_sum = [0] * (words_len+1)

    for i in range(words_len):
        if words[i][0] in vowel and words[i][-1] in vowel:
            prefix_sum[i+1] = prefix_sum[i]+1
        else:
            prefix_sum[i + 1] = prefix_sum[i]
    for left,right in queries:
        result.append(prefix_sum[right + 1] - prefix_sum[left])

    return result

                

        



if __name__ == '__main__':
    words = ["aba","bcb","ece","aa","e"]
    queries = [[0,2],[1,4],[1,1]]
    print(vowelStrings(words,queries))
    