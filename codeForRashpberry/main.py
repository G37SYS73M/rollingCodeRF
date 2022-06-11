#!/usr/bin/python3

import oNoFF,crypt,send


n = 10 
print("Fibbo Based Rolling Code Algo to Encode Data: \n By G37SYS73M\n")

while True:
	if n < 20:
		n+=1
		opt = int(input("Options:\nPress 1 for Start\nPress 2 for Stop\nPress 3 to Exit\n"))
		if(opt==1):
			signal = oNoFF.signalOn(n)
			print("\n\n",signal,"\n\n")
			send.send(signal)
		elif(opt==2):
			signal = oNoFF.signalOff(n)
			print("\n\n",signal,"\n\n")
			send.send(signal)
		elif(opt==3):
			print("Exiting....! Bye:)")
			exit()
		else:
			print("Invalid Input :(")
			print("Options:\nPress 1 for Star1t\nPress 2 for Stop\nPress 3 to Exit\n")
	else:
		n=10	


