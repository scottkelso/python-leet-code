def length_of_last_word(s: str) -> int:
    return len(s.split()[-1])

assert length_of_last_word("Hello World") == 5
assert length_of_last_word("   fly me   to   the moon  ") == 4
assert length_of_last_word("luffy is still joyboy") == 6