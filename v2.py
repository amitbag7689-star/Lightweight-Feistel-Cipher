import numpy as np
U = np.uint64

def rl(x, n):
    return (x << U(n)) | (x >> U(64 - n))

def ks(KA, KB, rounds):
    k, l = KA.copy(), KB.copy()
    rk = [k]
    for i in range(rounds - 1):
        l = (k + rl(l, 56)) ^ U(i) # ROTR 8 = ROTL 56
        k = rl(k, 3) ^ l
        rk.append(k)
    return rk

def F(R, K, a=3, b=8):
    return ((R ^ rl(R, a)) + K) ^ rl(R, b)

def enc(L, R, rk, a=3, b=8):
    for K in rk:
        L, R = R, L ^ F(R, K, a, b)
    return L, R

def dec(L, R, rk, a=3, b=8):
    for K in reversed(rk):
        L, R = R ^ F(L, K, a, b), L
    return L, R

def r64(rng, n):
    return rng.integers(0, 2**64, n, dtype=np.uint64)

def hw(x):
    c = np.zeros(x.shape, dtype=np.int64)
    for _ in range(64):
        c += (x & U(1)).astype(np.int64)
        x = x >> U(1)
    return c
