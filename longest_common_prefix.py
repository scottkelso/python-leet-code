def longest_common_prefix(strs: list[str]) -> str:
    min_length = len(min(strs, key=len))
    common_prefix = ""
    for i in range(min_length):
        character = strs[0][i]
        if all(word[i] == character for word in strs):
            common_prefix += character
        else:
            break
    return common_prefix

assert longest_common_prefix(["flower","flow","flight"]) == "fl"
assert longest_common_prefix(["dog","racecar","car"]) == ""
