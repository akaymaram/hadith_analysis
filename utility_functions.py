import pandas as pd
import datetime
import time
import sys
import os
import importlib

def arabic_to_english_numeral_converter(arabic_string):
	"""
	Note before use: python's built-in int() function works as an arabic to english numeral converter.
	Use this function if the python int() function is not working properly.
	ex: print(int('٢٣٤٥'))

	Converts a string containing Arabic numerals (٠-٩) to English numerals (0-9).

	This function iterates through each character in the input string. If the character is an Arabic numeral 
	(from '٠' to '٩'), it is converted to the corresponding English numeral. Non-numeric characters are left unchanged.
	The final result is returned as an integer, representing the converted number.

	Args:
		arabic_string (str): A string containing Arabic numerals and possibly other characters.

	Returns:
		int: The converted number in English numerals.

	Example:
		arabic_to_english_numeral_converter("٢٣٤٥") 
		# Output: 2345
		
		arabic_to_english_numeral_converter("١٢٣abc٤٥")
		# Output: 123abc45

	"""

	english_string = ''
	for char in arabic_string:
		if '٠' <= char <= '٩':
			english_string += str(ord(char) - ord('٠'))
		else:
			english_string += char
	return int(english_string)