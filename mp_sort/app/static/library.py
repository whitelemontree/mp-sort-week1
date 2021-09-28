from org.transcrypt.stubs.browser import *
import random

array = []

def gen_random_int(number, seed):
	pack = []
	for i in range(number):
		pack.append(i)
	random.seed(seed)
	random.shuffle(pack)
	result = pack
	return result


def generate():
	global array

	number = 10
	seed = 200

	# call gen_random_int() with the given number and seed
	# store it to the global variable array
	array = gen_random_int(number,seed)
	# convert the items into one single string 
	# the number should be separated by a comma
	# and a full stop should end the string.

	array_str = ""
	for nums in array:
		array_str = array_str+str(nums)+", "
	
	array_str = array_str[:-2:]+"."
	# This line is to placed the string into the HTML
	# under div section with the id called "generate"	
	document.getElementById("generate").innerHTML = array_str

def insertion_sort(lst):
	for index in range(1,len(lst)):
		swapped = True
		start = index 
		while start>0 and swapped:
			swapped = False
			if lst[start]<lst[start-1]:
				lst[start],lst[start-1] =lst[start-1],lst[start]
				start -= 1
				swapped = True
def bubble_sort(lst):
	n = len(lst)
	swapped = True
	while swapped:
		swapped = False
		for i in range(1,n):
			if lst[i-1] > lst[i]:
				lst[i],lst[i-1] = lst[i-1],lst[i]
				swapped = True
		n = n-1
	
		
		
def sortnumber1():
	'''	This function is used in Exercise 1.
		The function is called when the sort button is clicked.

		You need to do the following:
		- get the list of numbers from the global variable array and 
			copy it to a new list
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	sorted_array = array
	insertion_sort(sorted_array)
	array_str=""
	for nums in sorted_array:
		array_str = array_str +str(nums)+", "
	array_str = array_str[:-2:]+"."
	
	document.getElementById("sorted").innerHTML = array_str

def sortnumber2():
	'''	This function is used in Exercise 2.
		The function is called when the sort button is clicked.

		You need to do the following:
		- Get the numbers from a string variable "value".
		- Split the string using comma as the separator and convert them to 
			a list of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	# The following line get the value of the text input called "numbers"
	value = document.getElementsByName("numbers")[0].value

	# Throw alert and stop if nothing in the text input
	if value == "":
		window.alert("Your textbox is empty")
		return

	# Your code should start from here
	# store the final string to the variable array_str
	lst = value.split(",")
	lst_nums  = []
	array_str = ""
	for i in lst:
		
		if i.isdigit():
			lst_nums.append(int(i))
		if i[0] == "-" and i[1::].isdigit():
			lst_nums.append(-1*int(i[1:]))
	bubble_sort(lst_nums)
	for nums in lst_nums:
		array_str = array_str+ nums+", "
	array_str  = array_str[:-2:]+"."

	document.getElementById("sorted").innerHTML = array_str


## test