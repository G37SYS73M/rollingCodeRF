#!/usr/bin/python3

import oNoFF,crypt


n = 10 
print("Fibbo Based Rolling Code Algo to Encode Data: \n By G37SYS73M\n")

while True:
	if n < 20:
		n+=1
		opt = int(input("Options:\nPress 1 for Start Signal\nPress 2 for Stop Signal\nPress 3 to Exit\n"))
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
			print("Options:\nPress 1 for Star1t\nPress 2 for Stop\nPress 3 to Exit\n")
	else:
		n=10	


