def divBy42(divideBy):
    try:
        return 42 / divideBy
    except:
        print('Error: You tried to divide by zero.')


print(divBy42(2))
print(divBy42(12))
print(divBy42(0))
print(divBy42(1))
