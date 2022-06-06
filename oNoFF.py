import fibbo,rand,bi


def signalOn(n):
	fibbo_list= fibbo.fibbo(n)
	l_fibbo = len(fibbo_list)
	while True:
		rollin_num = rand.rollinNum(l_fibbo-1)
		if(fibbo_list[rollin_num]%2==0 and fibbo_list[rollin_num]!=0 ):
			x,y = bi.toBi(fibbo_list[rollin_num],rollin_num)
			return x,y
			break

def signalOff(n):
	fibbo_list= fibbo.fibbo(n)
	l_fibbo = len(fibbo_list)
	while True:
		rollin_num = rand.rollinNum(l_fibbo-1)
		if(fibbo_list[rollin_num]%2!=0 and fibbo_list[rollin_num]!=0):
			x,y = bi.toBi(fibbo_list[rollin_num],rollin_num)
			return x,y
			break