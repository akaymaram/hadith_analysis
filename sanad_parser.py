import pandas as pd
import pandas as pd
import re
import sys

file_path = sys.argv[1]
number_of_lines_to_read = sys.argv[2]

def read_first_n_lines_csv(file_path, number_of_lines_to_read):
    """
    Reads the first n lines of a CSV file using pandas.

    Args:
        file_path (str): The path to the CSV file.
        n (int): The number of lines to read.

    Returns:
        pandas.DataFrame: A DataFrame containing the first n lines of the CSV file, 
                          or None if an error occurs.
    """
    try:
        df = pd.read_csv(file_path, nrows=int(number_of_lines_to_read), encoding='utf-8')
        return df
    except FileNotFoundError:
        print(f"Error: File not found at path: {file_path}")
        return None
    except pd.errors.EmptyDataError:
         print(f"Error: The CSV file is empty: {file_path}")
         return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def string_to_list(input_string):
    cleaned_string = re.sub(r'[\[\]"\']', '', input_string)
    result_list = [item.strip() for item in cleaned_string.split(',')]
    return result_list



def sanad_parser(file_path=file_path, number_of_lines_to_read=number_of_lines_to_read):
  num_lines = number_of_lines_to_read
  df_head = read_first_n_lines_csv(file_path, num_lines)
  print(df_head)
  pd.set_option('display.max_rows', None)
  pd.set_option('display.max_columns', None)
  rows, cols = df_head.shape
  print(f"Number of rows: {rows}")
  print(f"Number of columns: {cols}")
  sanad = df_head['chain']
  print(df_head.columns)
  print(type(sanad[0]))
  key_value = {}
  value_key = {}
  key = 0
  for line in sanad:
   print(line)
   if line != "No SANAD":
    list_version = string_to_list(line)
    print(list_version)
    person_indices = []
    for person in list_version:
     if person not in value_key:
      
      key+=1
      key_value[key] = person
      value_key[person] = key
      person_indices.append(key)
     else:
      person_indices.append(value_key[person])
  return key_value


print(sanad_parser())

