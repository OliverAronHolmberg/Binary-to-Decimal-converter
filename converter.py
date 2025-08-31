
def binary_to_decimal_converter(binary_number):


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

    return decimal_number

binary_number = int(input("Write a binary number: "))
decimal_number = binary_to_decimal_converter(binary_number)

print(decimal_number)
