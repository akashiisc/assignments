import operator
import numpy as np
from copy import copy, deepcopy
from matrix_operations import *

def write_string_to_file(filePath , string_value):
	filePath.write(string_value+ "\n")

def print_beautifully(values_map , heading , Column1Heading , Column2Heading , write_to_file , filePath , type):
	filePath.write(heading + "\n")
	filePath.write("=======================================\n")
	if type == "map":
		filePath.write(Column1Heading + "\t" + Column2Heading + "\n")
		for i in values_map:
			filePath.write(str(i) + "\t|" + str(values_map[i]) + "\n")
	elif type == "list":
		filePath.write(",".join([str(g) for g in values_map]))
		filePath.write("\n")
	elif type == "list_of_list":
		for i in range(len(values_map)):
			filePath.write(",".join([str(g) for g in values_map[i]]))
			filePath.write("\n")
	elif type == "string":
		filePath.write(str(values_map))
		filePath.write("\n")
	filePath.write("=======================================\n") 


def print_barrier(filePath):
	filePath.write("=======================================\n") 	

def print_vspace(filePath):
	filePath.write("\n\n\n") 	

def print_beautifully_matrix( m, filePath , heading):
	filePath.write("\n\n\n")
	filePath.write(heading + "\n")
	filePath.write("=======================================\n") 		
	for i in range(len(m)):
		filePath.write(",".join([str(g) for g in m[i]]))
		filePath.write("\n")

def check_complex(list):
	complex_nos = 0
	for i in list:
		if isinstance(i, complex):
			complex_nos = complex_nos + 1
	return complex_nos

def find_unique_with_counts(apna_list):
	apna_map = {}
	position = 0;
	for i in apna_list:
		if i not in apna_map:
			apna_map[i] = [position]
		else :
			apna_map[i].append(position)
		position = position + 1
	return apna_map

def get_repeating_values(apna_map):
	return_map = {}
	for i in apna_map:
		if(len(apna_map[i]) > 1):
			return_map[i] = len(apna_map[i])
	return return_map;

def get_top_m_values(apna_map , m=1):
	sorted_by_value = sorted(apna_map , reverse=True)
	top_m_entries = []
	for i in range(m):
		top_m_entries.append(sorted_by_value[i])
	return top_m_entries

# def opr_transpose(m):
# 	rm = []


def append_m_columns(matrix , m ):
	copy_matrix = deepcopy(matrix)
	#temp = transpose(copy_matrix)
	temp = np.array(copy_matrix).transpose().tolist()
	for i in range(m):
		listofzeros = [0] * len(copy_matrix)
		temp.append(listofzeros)
	#temp = np.array(temp).transpose().tolist()
	return opr_transpose(temp)

def calculate_square_distance(m , i , j):
	sum_inner = 0
	for y in range(len(m[0])):
		sum_inner = sum_inner + ((m[i][y] - m[j][y])**2)
	return sum_inner

def take_top_m_points(values , m):
	top_m_entries = []
	for i in range(m):
		top_m_entries.append(values[i][0])
	return top_m_entries

def find_majority(num_list):
        idx, ctr = 0, 1
        
        for i in range(1, len(num_list)):
            if num_list[idx] == num_list[i]:
                ctr += 1
            else:
                ctr -= 1
                if ctr == 0:
                    idx = i
                    ctr = 1
        
        return num_list[idx]
