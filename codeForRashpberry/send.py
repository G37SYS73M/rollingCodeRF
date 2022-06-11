import os

def send(s):
    cmd = f"sudo ./sendook -f 433.0M -0 500 -1 250 -r 0 {s}"
    os.popen(cmd).read()