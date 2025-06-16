def full_justify(words: list[str], max_width: int)-> list[str]:
    text = [[]]
    row_cursor = 0
    width = 0
    for word in words:
        if width + len(word) <= max_width:
            text[row_cursor].append(word)
            width += len(word) + 1
        else:
            row_cursor += 1
            text.append([])

            text[row_cursor].append(word)
            width = len(word) + 1

    result = []
    for idx, row in enumerate(text):
        necessary_spaces = len(row) - 1
        needed_padding_size = max_width - sum(list(map(len, row)))

        # only one word -> space on end
        if necessary_spaces < 1:
            result.append(row[0] + ' '*needed_padding_size)

        # only two words & last line -> space on end
        elif necessary_spaces < 2 and idx+1 == len(text):
            result.append(' '.join(row) + ' '*(needed_padding_size-1))

        # more than two words -> space between words
        else:
            word_cursor = 0
            while needed_padding_size > 0:
                if word_cursor >= len(row) - 1:
                    word_cursor = 0
                row[word_cursor] = row[word_cursor] + ' '
                needed_padding_size -= 1
                word_cursor += 1

            result.append(''.join(row))

    return result

assert full_justify(["This", "is", "an", "example", "of", "text", "justification."], 16) == [
    "This    is    an",
   "example  of text",
   "justification.  "
]
assert full_justify(["What","must","be","acknowledgment","shall","be"], 16) == [
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
assert full_justify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20) == [
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
