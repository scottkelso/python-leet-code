def reverse_words(s: str) -> str:
    words = s.split()
    words.reverse()
    return ' '.join(words)

assert reverse_words("the sky is blue") == "blue is sky the"
assert reverse_words("  hello world  ") == "world hello"
assert reverse_words("a good   example") == "example good a"