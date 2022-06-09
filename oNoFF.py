import fibbo,rand,crypt,bi


def signalOn(n):
	fibbo_list= fibbo.fibbo(n)
	l_fibbo = len(fibbo_list)
	while True:
		rollin_num = rand.rollinNum(l_fibbo-1)
		if(fibbo_list[rollin_num]%2==0 and fibbo_list[rollin_num]!=0 ):
			x = crypt.encrypt(fibbo_list[rollin_num])
			y = bi.toBi(x)
			return y
			break

def signalOff(n):
	fibbo_list= fibbo.fibbo(n)
	l_fibbo = len(fibbo_list)
	while True:
		rollin_num = rand.rollinNum(l_fibbo-1)
		if(fibbo_list[rollin_num]%2!=0 and fibbo_list[rollin_num]!=0):
			x= crypt.encrypt(fibbo_list[rollin_num])
			y = bi.toBi(x)
			return y