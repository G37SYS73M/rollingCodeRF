#!/usr/bin/python3

import oNoFF,random

n = random.randint(0,99)

print("Fibbo Based Rolling Code Algo: \n By G37SYS73M\n")

while True:
	
	opt = int(input("Options:\nPress 1 for Start\nPress 2 for Stop\nPress 3 to Exit\n"))
	if(opt==1):
		signal = oNoFF.signalOn(n)
		print("\n\n",signal,"\n\n")
	elif(opt==2):
		signal = oNoFF.signalOff(n)
		print("\n\n",signal,"\n\n")
	elif(opt==3):
		print("Exiting....! Bye:)")
		exit()
	else:
		print("Invalid Input :(")
		print("Options:\nPress 1 for Start\nPress 2 for Stop\nPress 3 to Exit\n")
		


