import re

def traverse():
	# open file
	f = open('pyramid_sample_input.txt','r')
	# read target line
	row = f.readline()
	target_line = re.findall(r'\b\d+\b', row)
	target = int(target_line[0])
	print(target)
	#now start magic
	path = ""
	matrix = f.readlines()

	print_result(match_target(matrix, 0, 0, target, 1, path))
	f.close()


def match_target(matrix, line_number, index, target, prod, path):

	# if there's a next line at all
	if line_number+1 < len(matrix):
		curr_line = matrix[line_number]
		next_line = matrix[line_number+1]
		curr_value = curr_line[index]
		test_L = next_line[index]
		Lprod = prod*int(test_L)

		#always going to be a left child
		pathL = path + "L"
		#ye olde recursion
		return(match_target(matrix, line_number+1,index, target, Lprod, pathL))

		#if there's a right child at all
		if next_line[index+1] < len(next_line):
			test_R = next_line[index+1]
			pathR = path +"R"
			Rprod = prod *int(test_R)	
			#ye olde recursion
			return(match_target(matrix, line_number, index+1, target, Rprod, pathL))
		#no right child -- not worth pursuing
		else: return path

		#if we hit the target, yeehaw, print  our new path
		if Lprod == target:
			return pathL
		if Rprod == target:
			return pathR
	#if no next line, bounce it back
	return path

def print_result(print_path):
	if print_path == "": 
		return "no solution"
	else:
		reverse = print_path[::-1]
		print(reverse)
		return reverse




		

traverse()
