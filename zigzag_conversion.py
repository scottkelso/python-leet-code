def convert(s: str, num_rows: int) -> str:
    zigzag = [[] for row in range(num_rows)]
    row = 0
    zigging = True
    for i in range(len(s)):
        if zigging:
            zigzag[row].append(s[i])
            row += 1
        else:
            row -= 1
            zigzag[row].append(s[i])
        if row >= num_rows:
            zigging = False
            row -= 1
        if row <= 0:
            zigging = True
            row += 1

    result = []
    for row in zigzag:
        result.append("".join(row))

    return "".join(result)


assert convert("A", 1) == "A"
assert convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
assert convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
