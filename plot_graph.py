import pandas as pd
import pandas as pd
import re
import sys
import networkx as nx
import matplotlib.pyplot as plt
import dataframe_image as dfi


#! /usr/local/bin/python  -*- coding: UTF-8 -*-

file_path = sys.argv[1]
num_lines_to_read = int(sys.argv[2])
source_name = file_path[file_path.find('/')+1:].strip('.txt')
graph = nx.Graph()



def draw_circular(graph, with_labels = True):
 nx.draw_circular(graph,with_labels = with_labels)
 plt.savefig(source_name+"_graph.png")


# def create_graph_with_numbered_nodes(string_list):
#     """
#     Creates a NetworkX graph with nodes labeled with numbers based on a list of strings.

#     Args:
#         string_list: A list of strings.

#     Returns:
#         A NetworkX graph with nodes labeled with numbers corresponding to the index of the string in the input list.
#     """
#     thisdict = {}
#     for i, string in enumerate(string_list):
#         graph.add_node(i)  # Add node with number label
#         graph.nodes[i]['string_data'] = string # Store the original string as a node attribute if needed


# Verify the nodes and their attributes
def create_adjacent_edges(nodes):
  """
  Creates a NetworkX graph with edges connecting adjacent nodes in a list.

  Args:
    nodes: A list of nodes.

  Returns:
    A NetworkX graph with edges between adjacent nodes.
  """

  graph.add_nodes_from(nodes)
  for i in range(len(nodes) - 1):
    graph.add_edge(nodes[i], nodes[i + 1])






def string_to_list(input_string):
    cleaned_string = re.sub(r'[\[\]"\']', '', input_string)
    result_list = [item.strip() for item in cleaned_string.split(',')]
    return result_list

def read_first_n_lines_csv(file_path, n):
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
        df = pd.read_csv(file_path, nrows=n, encoding='utf-8')
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







# Example usage:
file_path = file_path  # Replace with the actual path to your CSV file
num_lines = num_lines_to_read
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
 if line != "No SANAD":
  list_version = string_to_list(line)
  person_indices = []
  for person in list_version:
   if person not in value_key:
    key+=1
    key_value[key] = person
    value_key[person] = key
    person_indices.append(key)
   else:
    person_indices.append(value_key[person])
  print(list_version)
  create_adjacent_edges(person_indices)

df_dic = pd.DataFrame.from_dict(key_value, orient='index', columns=['Value'])
dfi.export(df_dic, source_name+'_narrator_IDs.png')
plt.show()
draw_circular(graph)


