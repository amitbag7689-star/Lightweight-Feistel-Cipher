import numpy as np
import sys
from v2 import *

def generate_nist_sequence():
    print("Generating CTR mode sequences for NIST STS...")
    S = 100
    nb = 1_000_000
    out = open('v2_ctr.txt', 'w')
    # Logic to encrypt counters and unpack bits
    # ...
    out.close()
    print("File 'v2_ctr.txt' generated for NIST STS testing.")

if __name__ == "__main__":
    generate_nist_sequence()
