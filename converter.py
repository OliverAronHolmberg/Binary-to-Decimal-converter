binary_number = int(input("Write a binary number: "))

binary_list = list(str(binary_number))


decimal_list = []

exponent=0

for number in binary_list.__reversed__():
    number = int(number)
    
    x = number*2**exponent
    exponent+=1
    decimal_list.append(x)


decimal_number = 0

for decimal in decimal_list:
    decimal_number+=decimal

print(decimal_number)
