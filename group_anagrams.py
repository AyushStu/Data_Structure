# Problem: Group Anagrams
# Group strings that are anagrams into lists

from collections import defaultdict

def group_anagrams(strs):
    anagram_map = defaultdict(list)
    for word in strs:
        key = ''.join(sorted(word))
        anagram_map[key].append(word)
    return list(anagram_map.values())

# Example usage
if __name__ == "__main__":
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]