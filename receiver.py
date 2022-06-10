def decrypt(signal):
    sndrs_serial= 123456789
    rcvr_serial = 987654321
    key = sndrs_serial ^ rcvr_serial
    denc = signal // key
    fibbo(denc)

def fibbo(signal):
    l = list()
    t1 = 0
    t2 = 1
    t3=0
    while (t1<=signal):
        t3 = t1+t2
        l.append(t1)
        t1,t2=t2,t3
    signal_check(l,signal)

def signal_check(l,signal):
    if signal in l:
        if (signal %2 == 0):
            print("Start Signal Received!!!")
        else:
            print("Stop Signal Received!!!")
            
def main():
    used_code = list()
    while True:
        signal = int(input("Enter the Code"),2)
        if(len(used_code)<10 and signal not in used_code):
            used_code.append(signal)
            decrypt(signal)
        elif(len(used_code)>10):
            del used_code
        else:
            print("Invalid Signal")

main()