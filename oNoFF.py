import fibbo,rand

def signalOn():
	fibbo_list= fibbo.fibbo()
	
	while True:
		rollin_num = rand.rollinNum()
		if(fibbo_list[rollin_num]%2==0 and fibbo_list[rollin_num]!=0 ):
			return fibbo_list[rollin_num]
			break

def signalOff():
	fibbo_list= fibbo.fibbo()
	
	while True:
		rollin_num = rand.rollinNum()
		if(fibbo_list[rollin_num]%2!=0 and fibbo_list[rollin_num]!=0):
			return fibbo_list[rollin_num]
			break