def str_str(haystack: str, needle: str) -> int:
    return haystack.find(needle)


assert str_str("sadbutsad", "sad") == 0
assert str_str("leetcode", "leeto") == -1
