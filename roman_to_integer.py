def roman_to_int(s: str) -> int:
    count = s.count('I')
    count += s.count('V') * 5
    count += s.count('X') * 10
    count += s.count('L') * 50
    count += s.count('C') * 100
    count += s.count('D') * 500
    count += s.count('M') * 1000
    count -= s.count('IV') * 2 # IV would have been 1+5=6 but needs to be 4 so -2
    count -= s.count('IX') * 2 # IX would have been 1+10=11 but needs to be 9 so -2
    count -= s.count('XL') * 20 # XL would have been 10+50=60 but needs to be 40 so -20
    count -= s.count('XC') * 20 # XC would have been 10+100=110 but needs to be 90 so -20
    count -= s.count('CD') * 200 # CD would have been 100+500=600 but needs to be 400 so -200
    count -= s.count('CM') * 200 # CM would have been 100+1000=1100 but needs to be 900 so -200
    print(f'Counting {s} as {count}')
    return count


assert roman_to_int("I") == 1
assert roman_to_int("II") == 2
assert roman_to_int("III") == 3
assert roman_to_int("IV") == 4
assert roman_to_int("VIII") == 8
assert roman_to_int("LVIII") == 58
assert roman_to_int("MCMXCIV") == 1994

