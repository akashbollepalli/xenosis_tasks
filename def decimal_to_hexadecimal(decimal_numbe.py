def decimal_to_hexadecimal(decimal_number):
    # Handle the case when the input number is 0
    if decimal_number == 0:
        return "0"
    
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    
    while decimal_number > 0:
        remainder = decimal_number % 16
        hexadecimal = hex_chars[remainder] + hexadecimal
        decimal_number = decimal_number // 16
    
    return hexadecimal

# Test cases
print(decimal_to_hexadecimal(10))    # Output: A
print(decimal_to_hexadecimal(2545))  # Output: 9F1
print(decimal_to_hexadecimal(0))     # Output: 0
print(decimal_to_hexadecimal(255))   # Output: FF
