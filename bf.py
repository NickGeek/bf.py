#!/usr/bin/env python3
#TODO:
#while loop

from sys import argv as arg
from sys import exit

#Setup the memory
memory = [0]
cell = 0

#The interpreter
def interpret(code):
	#Setup vars
	global memory
	global cell
	output = ""

	#Sort the code to be processed character by character
	code = list(code)

	for c in code:
		if c == "+":
			#Increment the cell
			memory[cell] += 1
		elif c == "-":
			#Decrement the cell
			if memory[cell] > 0:
				memory[cell] -= 1
		elif c == ">":
			#Move to the next cell/create it
			cell += 1
			if len(memory)-1 < cell:
				memory.append(0)
		elif c == "<":
			#Move to the previous cell
			if cell > 0:
				cell -= 1
			else:
				print("Error: Data pointer out of range.")
		elif c == '.':
			#Print value of cell
			output += chr(memory[cell])
		elif c == ',':
			#Add the value of a string to the cell
			memory[cell] = ord(str(input(".. ")))
		elif c == "[":
			#Loop start
			pass
		elif c == "]":
			#Loop end
			pass


	#Return the memory
	return str(output)+"\n=> {"+str(memory[cell])+"} "+str(memory)

#The interactive shell
def interactive():
	print("bf.py 1.0.0\nhttp://github.com/NickGeek/bf.py")

	line = True
	while line:
		line = str(input("> "))
		if line:
			print(interpret(line))

try:
	filename = arg[1]
	codeFile = open(filename, "r")
	for line in codeFile:
		print(interpret(line))
except:
	interactive()