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
