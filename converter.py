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




list_of_acceptable_symbols = ["0", "1"]

while True:
    binary_number = input("Write a binary number: ")
    valid = True
    for symbol in binary_number:
        if symbol not in list_of_acceptable_symbols:
            print("Error, please input a binary number")
            valid = False
            break
    if valid:
        break
    
    

decimal_number = binary_to_decimal_converter(binary_number)
print(f"{binary_number} in decimal is equel to {decimal_number}")
