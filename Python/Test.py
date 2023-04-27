#A program that converts roman numerals to decimal numbers

numbers = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
}

def convert(num):
    total = 0
    for i in range(len(num)):
        if i > 0 and numbers[num[i]] > numbers[num[i-1]]:
            total += numbers[num[i]] - 2 * numbers[num[i-1]]
        else:
            total += numbers[num[i]]
    return total

#some complex test cases

test_cases = {
    "I": 1,
    "MDCLXVI": 1666,
    "MMXIX": 2019,
    "MMMDCCCLXXXVIII": 3888,
    "MMMDCCCLXXXVIIII": 3889,
    "MMMDCCCLXXXVIIII": 3889,
    "MMMDCCCLXXXVIIII": 3889,
    "XLIX": 49,
    "XCIX": 99,
    "CDXCIX": 499,
    "CMXCIX": 999,
    "MCMXCIX": 1999,
    "MMMCMXCIX": 3999,
}

for key, value in test_cases.items():
    print("Testing: ", key)
    print("Expected: ", value)
    print("Actual: ", convert(key))
    print("Passed: ", value == convert(key))
    print()
