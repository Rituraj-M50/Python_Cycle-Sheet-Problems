roman_c = { 1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100:'C'}
integer = int(input())
print_order = [100, 90, 50, 40, 10, 9, 5, 4, 1]

for x in print_order:
    if integer != 0:
        quotient = integer//x
        
        if quotient != 0:
            for y in range(quotient):
                print(roman_c[x], end="")
        integer = integer%x
