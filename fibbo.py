def fibbo():
	fibbo_list=list()
	t1=0
	t2=1
	for i in range(100):
		t3 = t1+t2
		fibbo_list.append(t1)
		t1,t2=t2,t3
	return fibbo_list