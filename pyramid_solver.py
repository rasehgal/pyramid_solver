import re

def traverse():
	path = ""
	#ask for file
	file_name = input("enter the name of the file containing the pyramid.\n (note: only .txt files are supported at this time)\n\n>>>")
	if ".txt" not in file_name:
		file_name = file_name + ".txt"
		# open file
	f = open(file_name,'r')
	# read target line
	row = f.readline()
	target_line = re.findall('(\d+)[^,]?+', row)
	#print("target_line: ")
	#print(target_line)
	target = int(target_line[0])
	print("target is : " + target_line[0])
	#now start magic
	matrix = f.readlines()
	#print("matrix: ")
	#print(matrix)
	trimmed = trim_pyramid(matrix)
	print(trimmed)
	match_target(trimmed, 0, 0, target, path, get_start(matrix))
	f.close()

def get_start(matrix):
	first_line = matrix[0]
	print("starting w " + first_line[0])
	return int(first_line[0])

def trim_pyramid(matrix):
	trimmed = []
	for line in matrix:
		line = re.findall('(\d+)[^,]?+', line)
		trimmed.append(line)
	return trimmed

#has to return an int
def match_target(matrix, index, line, target, path, prod):
	#print("alleyoop")
	#start_line = matrix[0]
	#start = int(start_line[0])
	#print("line: " + str(line))
	#print("index: " + str(index))
	#print("current path " + path)
	this_line = matrix[line]
	this_value = int(this_line[index])
	#print("we are on " + str(this_value))
	if path=="": new_prod = prod
	else: new_prod = prod*this_value
	#print("prod is now " + str(new_prod))
	#if not the last line
	if line == len(matrix)-1:
		#print("AT BOTTOM\n\n")
		if new_prod == target: 
			print("solution: " + path)
	else:
		next_line_num = line+1
		next_line = matrix[next_line_num]
		#print("not yet target")
		
		#print("print "+ this_line[index] + "// left recur on next line " + str(next_line_num) + ", index " + str(index))
		Lpath = path + "L"
		if (this_value * match_target(matrix, index, next_line_num, target, Lpath, new_prod)) == target:
		#	print("got target (L)")
			print("solution: " + Lpath)
		if next_line[index+1]: 
		#	print("print " + this_line[index] + "// right recur: next line " + str(next_line_num) + ", index " + str(index+1))
			Rpath = path + "R"
			if (this_value * match_target(matrix, index+1, next_line_num, target, Rpath, new_prod)) == target:
		#		print("got target (R)")
				print("solution: " + Rpath)

	#print("path not found")
	return 0
		


def print_result(print_path):
	if print_path == "": 
		return "no solution"
	else:
		reverse = print_path[::-1]
		print(reverse)
		return reverse




		

traverse()
