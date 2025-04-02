


def arabic_to_english_numeral_converter(arabic_string):
    english_string = ''
    for char in arabic_string:
        if '٠' <= char <= '٩':
            english_string += str(ord(char) - ord('٠'))
        else:
            english_string += char
    return int(english_string)



print(arabic_to_english_numeral(number))

sys.exit()