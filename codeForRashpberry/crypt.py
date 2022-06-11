import base64
from cmath import sin
sndrs_serial= 123456789
rcvr_serial = 987654321

def encrypt(signal):
    key = sndrs_serial ^ rcvr_serial
    enc = signal * key
    return enc
    


