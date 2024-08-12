# using array to form a unique key
# anagram words will have same key cause they have same chars
# result = { key: [words] },return result's values
from collections import defaultdict

def groupAnagrams(strs):
    result = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        key = tuple(count)
        result[key].append(s)
    
    return result.values()