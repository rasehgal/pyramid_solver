import re #import python regex library for digit matching


# handles file input and calls the various
# problem solver functions.
# user input: file name with or without '.txt' 
# extension (str)
# output: none
def snag_file():
	path = ""
	#ask for file and handle input without extension
	file_name = input("enter the name of the file containing the pyramid.\n (note: only .txt files are supported at this time)\n\n>>>")
	if ".txt" not in file_name:
		file_name = file_name + ".txt"


	# open file, read the first line for the target number,
	# and strip any extraneous characters. then grab the
	# target number in int form
	f = open(file_name,'r')
	row = f.readline()
	target_line = re.findall('(\d+)[^,]?+', row)
	target = int(target_line[0])
	
	# grab the remainder of the file and input into a matrix
	# matrix is composed of lines, lines are composed of the digits
	# from the input file 
	matrix = f.readlines()
	trimmed = trim_pyramid(matrix)
	match_target(trimmed, 0, 0, target, path, get_start(matrix))

	# close the file and exit
	f.close()



# get the first line of the pyramid to 
# initialize our product so as to
# multiply correctly

# input: matrix of strings ([str,...])
# output: very first number in pyramid (int)

def get_start(matrix):
	first_line = matrix[0]
	return int(first_line[0])


# take the remainder of the lines and trim
# extra characters like commas and spaces

# input: matrix of strings [str,...]
# output: matrix of digit-only strings [str,...]
def trim_pyramid(matrix):
	trimmed = []
	for line in matrix:
		line = re.findall('(\d+)[^,]?+', line)
		trimmed.append(line)
	return trimmed

# compare paths to determine which multiplies out
# to our target number

#input: 
#	- [str,..]	matrix of lines
#	- (int)	starting line in matrix (we default to 0)
#	- (int)	starting index in line (we default to 0)
#	- (int)	target value 
#	- (str)	path string
#	- (int)	current resulting product

#output: none (print statements)
def match_target(matrix, line, index, target, path, prod):

	# handy references to the current line/value/product
	this_line = matrix[line]
	this_value = int(this_line[index])
	# checking if we're just starting or not
	if path=="": new_prod = prod
	else: new_prod = prod*this_value

	# if this is the last line of the matrix/file
	# check if we have a solution
	if line == len(matrix)-1:
		if new_prod == target: 
			print("solution: " + path)			
	# not yet at the last line;
	# we iterate
	else:
		next_line_num = line+1
		next_line = matrix[next_line_num]

		# recur on the left and note that we went left;
		# print path if we get a solution
		Lpath = path + "L"
		if (this_value * match_target(matrix, next_line_num, index, target, Lpath, new_prod)) == target:
			print("solution: " + Lpath)
		# check if there is a right index; if so then
		# recur on right side and print path to any
		# solutions we find
		if next_line[index+1]: 
			Rpath = path + "R"
			if (this_value * match_target(matrix, next_line_num, index+1, target, Rpath, new_prod)) == target:
				print("solution: " + Rpath)

	return 0
		

# start program and ask for input file
snag_file()
